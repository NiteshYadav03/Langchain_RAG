from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from typing import Literal
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda

load_dotenv()

model=ChatOpenAI()
parser= StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['Negative','Positive']

pyparser=PydanticOutputParser(pydantic_object=Feedback)




prompt1=PromptTemplate(template='Give the sentiment for {topic}\n {format_instruction}',input_variable=['topic'],partial_variables={'format_instruction':pyparser.get_format_instructions()})

classifier_chain= prompt1 | model | pyparser

# result=classifier_chain.invoke({'topic':'This is not good at all'}).sentiment

# print(result)

prompt2=PromptTemplate(template='Write response for this positive Feedback {feedback}',input_variable=['feedback'])

prompt3=PromptTemplate(template='Write response for this negative Feedback {feedback}',input_variable=['feedback'])

pos_feedback_chain=prompt2 | model | parser

neg_feedback_chain=prompt3 | model | parser

branch_chain=RannableBranch (
    (lambda x:x.sentiment=='Positive',pos_feedback_chain),
    (lambda x:x.sentiment=='Negative',neg_feedback_chain),
    RunnableLambda(lambda x: "could not find anything")
    )


chain = classifier_chain | branch_chain

result =chain.invoke({'feedback':"This is terribel man"})

print(result)

chain.get_graph().print_ascii()
