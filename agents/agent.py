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

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

prompt.format(product="colorful socks")
prompt = "What is a good name for a company that makes colorful socks?"
print(llm(prompt))

class EventAgent():
    
    def say_hello(self):
        prompt = "What is a good name for a company that makes colorful socks?"
        print(llm(prompt))

    def connect_chatgpt(self, user_input):
        print(llm(user_input))
        