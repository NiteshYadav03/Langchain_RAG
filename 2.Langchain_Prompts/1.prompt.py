from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)
topic = "Feature Engineering"

prompt_template = load_prompt("template_prompt.json")


prompt=prompt_template.invoke({"topic": topic})

result = model.invoke(prompt)
print(result.content)
