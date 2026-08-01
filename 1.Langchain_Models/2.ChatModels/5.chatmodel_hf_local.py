from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline




llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm, temperature=0.9, max_tokens=150)

result=model.invoke("Write a short poem about the beauty of nature.")
print(result.content)