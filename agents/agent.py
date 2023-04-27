import langchain
import openai
import os

from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")

llm = OpenAI(temperature=0.9)

class EventAgent():
    
    def say_hello(self):
        prompt = "Say hello in a random and fun way"
        print(llm(prompt))

    def connect_chatgpt(self, user_input):
        print(llm(user_input))
        