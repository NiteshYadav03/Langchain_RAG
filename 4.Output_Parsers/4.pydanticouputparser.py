from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field


load_dotenv()

llm = HuggingFaceEndpoint(model_name="google/flan-t5-xxl",task="text2text-generation")
model=ChatHuggingFace(llm=llm,temperature=0.9,max_tokens=150)

class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(..., description="The age of the person")
    email: str = Field(..., description="The email address of the person")

parser=PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(template="You are a helpful assistant. Create a JSON object with the following fields: name, age, email. The values should be based on the input topic: {topic}.",input_variables=["topic"],partial_variables={"parser":parser.get_format_instructions()})


# prompt= template.invoke({"topic":"Feature Engineering"})

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template | model | parser

result = chain.invoke({"topic":"Feature Engineering"})
print(result)
