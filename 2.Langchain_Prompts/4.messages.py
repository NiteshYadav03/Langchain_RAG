from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150) 

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain the concept of Feature Engineering in simple terms.")
]

result = model.invoke(messages)
# print(result.content)
messages.append(AIMessage(content=result.content))

print(messages)

