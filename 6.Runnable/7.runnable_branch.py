from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableBranch


load_dotenv()


prompt1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Write a summary of {report}",
    input_variables=['report']
)

model = ChatOpenAI()

parser=StrOutputParser()

chain_for_report=RunnableSequence(prompt1,model,parser)
chain_for_summary=RunnableSequence(prompt2,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.slit())>500,chain_for_summary),
    RunnablePassthrough

)

final_chain=RunnableSequence(chain_for_report,branch_chain)

final_chain.invoke({'topic':'Indian Politics'})




