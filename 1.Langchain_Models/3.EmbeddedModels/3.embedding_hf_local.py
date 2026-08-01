from langchain_openai import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text="what is the capital of France?"
documents = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome.",
]

# vector=embeddings.embed_query(text)
vector=embeddings.embed_documents(documents)
print(str(vector))