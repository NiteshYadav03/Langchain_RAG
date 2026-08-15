from langchain.text_splitter import RecursiveCharacterTextSplitter

text="""Text you want to split"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(result) # result is list of string