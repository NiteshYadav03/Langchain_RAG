from langchain_community.document_loader import CSVLoader


loader = CSVLoader(file_path='folder path')

docs = loader.load()
print(docs)
# docs is a list
