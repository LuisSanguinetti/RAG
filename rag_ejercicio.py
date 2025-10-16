# python -m venv .venv
# .venv\Scripts\Activate.ps1
# pip install langchain langchain_community langchain_ollama
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path

# 1. Cargar texto propio (ej. un .txt o artículo)
data_path = Path(__file__).resolve().parent / "data"
docs = []
for p in data_path.glob("*.txt"):
    docs.extend(TextLoader(p.as_posix(), encoding="utf-8").load())

# 2. Dividir en chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# 3. Crear embeddings y FAISS
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(chunks, embeddings)
retriever = db.as_retriever()

# 4. Crear LLM y prompt
llm = OllamaLLM(
    model="deepseek-r1:1.5b",
    base_url="http://127.0.0.1:11434"
)
prompt = ChatPromptTemplate.from_template("Usa este contexto para responder:\n{context}\nPregunta: {input}\nRespuesta:")

# 5. Pipeline
question = input("Pregunta: ")
docs = retriever.invoke(question)
context = "\n\n".join(d.page_content for d in docs)
answer = llm.invoke(prompt.format(context=context, input=question))
print(answer)
