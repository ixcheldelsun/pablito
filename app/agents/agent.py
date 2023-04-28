
import os

from dotenv import load_dotenv
load_dotenv()
from langchain import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms import OpenAI


from app.models.llm import Pablito
from app.agents import event_contexts


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#SERP_API_KEY = os.getenv("SERP_API_KEY")

llm = OpenAI(temperature=0.8)


event_context = event_contexts.version_1

event_system_messages_no_input = '''
You are a helpful but conservative coordinator for an event that is very intent on giving people factually correct information. You help people assisting the event or planning the event know where they need to be, what they need to be prepared, what is important to know, and anything that they might require related to the event.
This is the event information:
{}
Answer the following question based on the information above. If the answer is not provided in the information above, give a logical answer without being too specific.
If you don't know the answer, just say that you don't know, don't try to make up an answer. Instead, make suggestions on what they can do to find the answer.
'''

previous_responses = []
input_setup = """
QUESTION: {}
ANSWER:
"""


class EventAgent():

    def say_hello(self, user_input):
        return llm('say hello')

    def connect_chatgpt(self, user_input):
        print(llm(user_input))

    def create_prompt(self, user_input):
        event_system_messages = event_system_messages_no_input + input_setup
        return event_system_messages.format(event_context, user_input)
    

    def answer_event_FAQs(self, user_input):
        prompt = self.create_prompt(user_input)
        print(llm(prompt))
        return llm(prompt)


    def run_event_agent(self, user_input):
        from langchain.agents import load_tools
        from langchain.agents import initialize_agent
        from langchain.agents import AgentType
        from langchain.chat_models import ChatOpenAI
        from langchain.llms import OpenAI

        # First, let's load the language model we're going to use to control the agent.
        chat = ChatOpenAI(temperature=0)

        # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
        llm = OpenAI(temperature=0)
        tools = load_tools(["serpapi"], llm=llm, serpapi_api_key=SERP_API_KEY)


        # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
        agent = initialize_agent(tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

        prompt = self.create_prompt(user_input)

        # Now let's test it out!
        agent.run(prompt)

    def run_chat(self, user_input):
        from langchain.prompts import (
            ChatPromptTemplate, 
            MessagesPlaceholder, 
            SystemMessagePromptTemplate, 
            HumanMessagePromptTemplate
        )
        from langchain.chains import ConversationChain
        from langchain.chat_models import ChatOpenAI
        from langchain.memory import ConversationBufferMemory


        pre_prompt = event_system_messages_no_input.format(event_context)
        print('event_system_messages_no_input')
        print(pre_prompt)
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(pre_prompt),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{user_input}")
        ])

        llm = ChatOpenAI(temperature=0)
        memory = ConversationBufferMemory(return_messages=True)
        conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)


    
    def _conversation_chat(self, user_input):
        prompt = self.create_prompt(user_input)
        memory = ConversationBufferWindowMemory(prompt=prompt, k=10)
        conversation = ConversationChain(llm=llm(prompt), 
                                verbose=False,
                                memory=memory)
        
        return conversation.predict(input=user_input)

    previous_responses = []

    def conversation_chat(self, user_input):
        prompt = self.create_prompt(user_input)
        # Concatenar el prompt y las respuestas anteriores
        full_prompt = prompt + "\n" + "\n".join(previous_responses) + "\n"
        memory = ConversationBufferWindowMemory(prompt=prompt, k=10)
        conversation = ConversationChain(llm=llm(prompt), 
                                verbose=False,
                                memory=memory)

        # Generar la respuesta de la conversación
        answer = conversation.predict(full_prompt + user_input)

        # Agregar la respuesta actual a la lista de respuestas anteriores
        previous_responses.append(user_input + "\n" + answer)

        # Actualizar la memoria de conversación
        conversation.memory.add(full_prompt + user_input, answer)

        return answer