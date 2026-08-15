from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text="""Text you want to split like code or markdown"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(result) # result is list of string