from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


chat_template=ChatPromptTemplate([
    ('system', "You are a expert in {domain}."),
    MessagesPlaceholder(variable_name="history"),
    ('human', "Explain the concept of {topic} in simple terms.")
])

chat_history=[]

with open("chat_history.txt","r") as f:
    history = f.readlines()
    chat_history.append(history)

prompt=chat_template.invoke({"chat_history": chat_history,"domain": "artificial intelligence","topic": "machine learning"})

