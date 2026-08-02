from langchain_core.prompts import PromptTemplate


topic = "Feature Engineering"
template = PromptTemplate(
    input_variables=["topic"],
    template="Explain the concept of {topic} in simple terms."

)

template.save("template_prompt.json")