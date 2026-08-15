from langchain_core.tools import tool

@tool
def multi(a:int,b:int)->int:
    """Multiply two number"""
    return a*b

result=multi.invoke({"a":2,"b":3})

print(result)

print(multi.name)
print(multi.description)
print(multi.args) 