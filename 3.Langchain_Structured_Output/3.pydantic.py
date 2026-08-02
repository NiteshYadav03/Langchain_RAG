from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    email: str

newPerson = Person(name="John Doe", age=30, email="John@gmail.com")
print(newPerson)