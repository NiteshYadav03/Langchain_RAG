from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int
    email: str

newPerson: Person = {
    "name": "John Doe",
    "age": 30,
    "email": "john@gmail.com"
}