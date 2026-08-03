from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)


prompt_template1 = PromptTemplate(
    template="Explain the concept of {topic} in simple terms.",
    input_variables=["topic"]
)

prompt_template2 = PromptTemplate(
    template="give me 5 important points about {concept}?",
    input_variables=["concept"]
)

parser = StrOutputParser()


chain = prompt_template1 | model | parser | prompt_template2 | model | parser

result = chain.invoke({"topic": "Feature Engineering"})
print(result)

chain.get_graph().print_ascii()

