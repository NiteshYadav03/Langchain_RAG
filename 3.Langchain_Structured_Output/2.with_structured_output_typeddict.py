from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Literal, TypedDict,Annotated,Optional


load_dotenv()
model = ChatOpenAI(model_name="gpt-4", temperature=0.9, max_tokens=150)

class FeatureEngineeringOutput(TypedDict):
    definition: Annotated[str, "A clear and concise definition"]
    example: Annotated[str, "A practical example"]
    key_themes: Annotated[list[str], "A list of key themes or concepts"]
    pros: Annotated[Optional[list[str]], "A list of advantages or benefits"]
    cons: Annotated[Optional[list[str]], "A list of disadvantages or drawbacks"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "The overall sentiment or tone of the explanation"]

structured_model=model.with_structured_output(FeatureEngineeringOutput)

result = structured_model.invoke("Explain the concept of Feature Engineering in simple terms.")
print(result)
