from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text="""Text you want to split"""

splitter=SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1,
)

result = splitter.create_documents([text])

print(result) # result is list of string