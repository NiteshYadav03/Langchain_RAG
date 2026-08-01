from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(model_name="claude-3", temperature=0.9, max_tokens=150)

result = chat_model.invoke("What is regression?")
print(result.content)