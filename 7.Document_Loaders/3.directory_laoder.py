from langchain_community.document_loader import DirectoryLoader,PyPDFLoader


loader = DirectoryLoader(path='folder path',glob='*.pdf',loader_cls=PyPDFLoader)

docs = loader.load()
print(docs)
# docs is a list
