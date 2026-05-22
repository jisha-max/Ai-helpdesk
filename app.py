from flask import Flask, request, jsonify, render_template
print("🚀 Help desk...")

# from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


# ----------------------------
# Flask App
# ----------------------------
app = Flask(__name__)


# ----------------------------
# Load and prepare data
# ----------------------------

loader = PyPDFLoader("College Information System.pdf")
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(docs, embedding)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)


# ----------------------------
# Load LLM
# ----------------------------
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=100
)

llm = HuggingFacePipeline(pipeline=generator)


# ----------------------------
# Create QA system
# ----------------------------
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)


# ----------------------------
# Static student data
# ----------------------------
students = {
    "john": "John - CSE - 3rd Year - 9876543210",
    "anita": "Anita - ECE - 2nd Year - 9123456780",
    "rahul": "Rahul - ME - 4th Year - 9988776655"
}


# ----------------------------
# Home Route
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")
# ----------------------------
# Ask Route
# ----------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"answer": "Please send a question"}), 400

    question = data["question"].lower().strip()

    if question in ["hi", "hello", "hey"]:
        return jsonify({"answer": "Hello! 👋 Do you need any help?"})

    words = question.split()

    for word in words:
        if word in students:
            return jsonify({"answer": students[word]})

    answer = qa.invoke({"query": question})["result"]

    return jsonify({"answer": answer})


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)