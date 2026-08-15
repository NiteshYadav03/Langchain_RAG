from langchain_core.tools import tool

@tool
def add(a:int,b:int)->int:
    """Add two numbers"""
    return a+b

@tool
def multi(a:int,b:int)->int:
    """Multiply two number"""
    return a*b


class MathToolkit:
    def get_tools(self):
        return [add,multi]

toolkit=MathToolkit()

tools=toolkit.get_tools()