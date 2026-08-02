from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)

chat_prompt_template=ChatPromptTemplate([('system', "You are a expert in {domain}."), ('human', "Explain the concept of {topic} in simple terms.")])

chat_prompt=chat_prompt_template.invoke({"domain": "Feature Engineering", "topic": "Feature Engineering"})
print(chat_prompt)
