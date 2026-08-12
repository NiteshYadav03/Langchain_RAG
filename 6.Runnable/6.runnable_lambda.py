from langchain.schema.runnable import RunnableLambda

def word_count(text):
    return len(text.split())


word_count_runnable=RunnableLambda(word_count)

word_count_runnable.invoke("This is an string")