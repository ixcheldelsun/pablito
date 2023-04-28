# import langchain
# import openai
# import os

# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain import ConversationChain
# from langchain.chat_models import ChatOpenAI

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# SERP_API_KEY = os.getenv("SERP_API_KEY")

# llm = OpenAI(temperature=0.9)

# prompt = PromptTemplate(
#     input_variables=["product"],
#     template="What is a good name for a company that makes {product}?",
# )

# prompt.format(product="colorful socks")
# prompt = "What is a good name for a company that makes colorful socks?"
# print(llm(prompt))


from app.agents.agent import EventAgent

agent = EventAgent()
# agent.say_hello()
# agent.connect_chatgpt("What is the capital of Romania?")
# prompt = agent.create_prompt('What is this about?')
# print(prompt)
# agent.answer_event_FAQs('Me puedes dar la direccion de Oliva?')
agent.answer_event_FAQs('Me puedes dar la direccion de Oliva?')
# agent.run_chat('What is the first event where I need to be?')
# product = 'colorful socks'
# print(prompt.format(product=product))

# chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
# chain.run("colorful socks")


# llm = OpenAI(temperature=0)
# conversation = ConversationChain(llm=llm, verbose=True)

# output = conversation.predict(input="Hi there!")
# print(output)


# from langchain.schema import (
#     AIMessage,
#     HumanMessage,
#     SystemMessage
# )

# chat = ChatOpenAI(temperature=0)

# system_message = "You are a helpful coordinator for an event. You help people assisting the event or planning the event know where they need to be, what they need to be prepared, what is important to know, and anything that they might require related to the event."
# messages = [
#     SystemMessage(content="You are a helpful coordinator for an event."),
#     HumanMessage(content="Hi there")
# ]
# result = chat.generate(messages)
# # result = chat.generate(messages)
# result

# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.agents import AgentType

# # First, let's load the language model we're going to use to control the agent.
# llm = OpenAI(temperature=0, serp_api_key=SERP_API_KEY)

# # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
# tools = load_tools(["serpapi"], llm=llm)


# # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# # Now let's test it out!
# agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")