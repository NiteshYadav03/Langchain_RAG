from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)


prompt_template = PromptTemplate(
    template="Explain the concept of {topic} in simple terms.",
    input_variables=["topic"]
)

parser = StrOutputParser()

# prompt = prompt_template.invoke({"topic": "Feature Engineering"})

# result=parser.parse(prompt)

# final_result = model.invoke(result)
# print(final_result.content)

chain = prompt_template | model | parser

result = chain.invoke({"topic": "Feature Engineering"})
print(result)

chain.get_graph().print_ascii()

