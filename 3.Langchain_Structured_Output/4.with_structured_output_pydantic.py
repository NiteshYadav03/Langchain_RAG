from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import Optional

load_dotenv()
model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)

class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(..., description="The age of the person")
    email: str = Field(..., description="The email address of the person")

structured_model=model.with_structured_output(Person)

result = structured_model.invoke("Create a person with name 'Alice', age 25, and email 'alice@gmail.com'")
print(result)