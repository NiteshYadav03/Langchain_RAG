from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


llm = HuggingFaceEndpoint(model_name="google/flan-t5-xxl",task="text2text-generation")
model=ChatHuggingFace(llm=llm,temperature=0.9,max_tokens=150)


template1=PromptTemplate(template="You are a helpful assistant. Explain the concept of {topic} in simple terms.",input_variables=["topic"])

template2=PromptTemplate(template="give the summary of {topic}.",input_variables=["topic"])

# prompt1=template1.invoke({"topic":"Feature Engineering"})
# prompt2=template2.invoke({"topic":"Feature Engineering"})

# result1=model.invoke(prompt1)
# result2=model.invoke(prompt2)

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic":"Feature Engineering"})
print(result)