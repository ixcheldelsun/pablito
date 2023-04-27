import langchain
import openai
import os

from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
product = 'colorful socks'
print(prompt.format(product=product))


chain = LLMChain(llm=llm, prompt=prompt)