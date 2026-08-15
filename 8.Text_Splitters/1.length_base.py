from langchain.text_splitter import CharacterTextSplitter

text="""Text you want to split"""

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result) # result is list of string