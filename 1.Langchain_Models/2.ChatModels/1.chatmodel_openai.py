from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model_name="gpt-5.6", temperature=0.9, max_tokens=150,max_completion_tokens=1000)

result = chat_model.invoke("Write about india.")
print(result.content)