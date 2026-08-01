from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

#history of computer
documents=[
    "The history of computers dates back to the early 19th century when Charles Babbage designed the first mechanical computer", 
    "known as the Analytical Engine. This machine laid the foundation for modern computing by introducing concepts such as programmable instructions and a central processing unit (CPU).",
    " Over the years, computers have evolved from large, room-sized machines to compact devices that fit in our pockets.", 
    "The development of transistors, integrated circuits and microprocessors revolutionized computing, making it faster, more efficient, and accessible to the masses.", 
    "Today, computers are an integral part of our daily lives, powering everything from smartphones and laptops to artificial intelligence and cloud computing.",
    
]

document_embeddings = embeddings.embed_documents(documents)
print(str(document_embeddings))

query = "What is full form of CPU?"

query_embedding = embeddings.embed_query(query)
print(str(query_embedding))



similarity = cosine_similarity([query_embedding], document_embeddings)
best_match_index = 0
for i in range(len(similarity[0])):
    if similarity[0][i] > similarity[0][best_match_index]:
        best_match_index = i

print(f"Best matching document: {documents[best_match_index]}, with similarity score: {similarity[0][best_match_index]}")