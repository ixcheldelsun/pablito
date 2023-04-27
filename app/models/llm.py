from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

import os
from dotenv import load_dotenv

load_dotenv()

class Pablito:
    
    def __init__(self) -> None:
        self.key = os.environ['OPENAI_API_KEY']
        self.llm = OpenAI(openai_api_key=self.key)
        #self.topic = topic
        self.input_template = PromptTemplate(
            input_variables = ['topic'],
            template=f'You are an event planning expert. People will ask you about advices about'
        )
        self.conversation_memory = ConversationBufferMemory(
            input_key='topic',
            memory_key='chat_history'
        )
        self.input_chain = LLMChain(
            llm=self.llm,
            prompt=self.input_template,
            verbose=True,
            memory=self.conversation_memory
        )
        

    def run(self, prompt):

        input = self.input_chain.run(input(prompt))
        
        return input

# User Input
# input_template = PromptTemplate(
#     input_variables = ['topic'],
#     template='You are an event planning expert. People will ask you about advices about {topic}'
# )

# Memory 
# conversation_memory = ConversationBufferMemory(input_key='topic',
#                                                memory_key='chat_history')

# Llms
# input_chain = LLMChain(llm=llm,
#                        prompt=input_template,
#                        verbose=True,
#                        memory=conversation_memory)


