from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests


@tool
def multi(a:int,b:int)->int:
    """Multiply two number"""
    return a*b

result = multi.invole({'a':3,'b':4});

print(result)

llm= ChatOpenAI()

llm_with_tools=llm.bind_tools([multi]) # tool binding

