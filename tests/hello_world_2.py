from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

OPENAI_API_KEY ='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'

llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# User Input
input_template = PromptTemplate(
    input_variables = ['topic'],
    template='You are an event planning expert. People will ask you about advices about {topic}'
)

# Memory 
conversation_memory = ConversationBufferMemory(input_key='topic',
                                               memory_key='chat_history')

# Llms
input_chain = LLMChain(llm=llm,
                       prompt=input_template,
                       verbose=True,
                       memory=conversation_memory)

prompt = input("que desea saber: ")

input = input_chain.run(prompt)

print(input)