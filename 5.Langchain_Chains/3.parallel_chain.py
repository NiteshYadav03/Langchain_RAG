from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model=ChatOpenAI()

prompt1=PromptTemplate(template="Generate notes on {topic}",input_variables=["topic"])

prompt2=PromptTemplate(template="Generate 5 question on {topic}",input_variables=["topic"])

prompt3=PromptTemplate(template="Make a combination note of {note} and {question}",input_variables=["note","question"])

parser=StrOutputParser()

parallel_chain=RunnabelParallel({
    'note':prompt1 | model | parser,
    'question':prompt2 | model | parser
})

merge_chain=prompt3 | model | parser

chain= parallel_chain | merge_chain

result = chain.invoke({'topic':'Indian cinema'})

print(result)

chain.get_graph().print_ascii()
