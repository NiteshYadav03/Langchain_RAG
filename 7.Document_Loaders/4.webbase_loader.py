from langchain_community.document_loader import WebBaseLoader


loader = WebBaseLoader(url='htttp://wwww.goole.com/page/2')

docs = loader.load()
print(docs)
# docs is a list
