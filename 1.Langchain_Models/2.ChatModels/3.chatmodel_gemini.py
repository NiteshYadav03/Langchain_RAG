from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenAI(model_name="gemini-1.3", temperature=0.9, max_tokens=150)
result = chat_model.invoke("What is Feature Engineering?")
print(result.content)