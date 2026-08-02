from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()
model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)

person_schema = {
    "title": "Person",
    "type": "object",
    "description": "A person object with name, age, and email.",
    "properties": {
        "name": {
            "type": "string",
            "description": "The name of the person."
        },
        "age": {
            "type": "integer",
            "description": "The age of the person."
        },
        "email": {
            "type": "string",
            "description": "The email address of the person."
        }
    },
    "required": ["name", "age", "email"]
}

structured_model=model.with_structured_output(person_schema)

result = structured_model.invoke("Create a person with name 'Alice', age 25, and email 'alice@gmail.com'")
print(result)