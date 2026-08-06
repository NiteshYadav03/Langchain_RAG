import random
from abc import ABC,abstractmethod


class Runnable(ABC):

    @abstractmethod
    def invoke(self):
        pass

class AsliLLM(Runnable):

    def __init__(self):
        print("LLM created")

    def predict(self,prompt):

        response_list=[
            "Delhi is capital of india",
            "IPL is Premiur leage",
            "2+2 is 4"
        ]
        return {'response':random.choice(response_list)}
    def invoke(self,prompt):
        
        response_list=[
            "Delhi is capital of india",
            "IPL is Premiur leage",
            "2+2 is 4"
        ]
        return {'response':random.choice(response_list)}
    




class AsliPromptTemplate(Runnable):

    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict)

    def invoke(self,input_dict):
        return self.template.format(**input_dict)


    
class RunnabelConnector(Runnable):

    def __init__(self,runnable_list):
        self.runnable_list=runnable_list

    def invoke(self,input_data):

        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)
        return input_data

template=AsliPromptTemplate(
    template="Write an poem on {topic}",
    input_variables="topic"
)
llm=AsliLLM()

chain=RunnabelConnector([template,llm])

result=chain.invoke({'topic':'India'})

print(result)







