from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model_name="gpt-3.5-turbo", temperature=0.9, max_tokens=150)

result=llm.invoke("Write a short poem about the beauty of nature.")

print(result)