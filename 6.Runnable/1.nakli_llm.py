import random

class NakliLLM:

    def __init__(self):
        print("LLM created")

    def predict(self,prompt):

        response_list=[
            "Delhi is capital of india",
            "IPL is Premiur leage",
            "2+2 is 4"
        ]
        return {'response':random.choice(response_list)}

# llm=NakliLLM()
# print(llm.predict("What is this bro?"))


class NakliPromptTemplate:

    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict)


template=NakliPromptTemplate(template="write poem about the {topic}",input_variables=["topic"])

# prompt=template.format({'topic':'india'})

llm=NakliLLM()
# result=llm.predict(prompt)

# print(result)


class NakliLLMChain:

    def __init__(self,llm,prompt):
        self.llm=llm
        self.prompt=prompt

    def run(self,input_dict):
        llm_prompt=self.prompt.format(input_dict)
        result=self.llm.predict(llm_prompt)

        return result['response']


llmchain=NakliLLMChain(llm,template)

result=llmchain.run({'topic':'india'})

print(result)



