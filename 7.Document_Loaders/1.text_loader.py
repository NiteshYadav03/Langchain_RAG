from langchain_community.document_loader import TextLoader


loader = TextLoader(path='path of file',encoding='uft-8')

docs = loader.load()
print(docs)
# docs is a list
