from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)

messages = []
while True:
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print(messages)
   
