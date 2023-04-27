import os
from dotenv import load_dotenv
from twilio.rest import Client
from fastapi import FastAPI, Form

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

app = FastAPI()


def send_message(body_text):
    client.messages.create(
        from_="whatsapp:+14155238886", body=body_text, to="whatsapp:+584122370830"
    )


@app.post("/message")
def init_bot(Body: str = Form()):
    message = Body.lower() # get the message the user sent our bot
    response = f"Hello, I am a bot. I am still learning. I got the following message from you: {str(message)}."
    # user_msg = request.values.get('Body', '').lower()
 
    # # creating object of MessagingResponse
    # response = MessagingResponse()
 
    # # User Query
    # q = user_msg + "geeksforgeeks.org"
 
    # # list to store urls
    # result = []
 
    # # searching and storing urls
    # for i in search(q, tld='co.in', num=6, stop=6, pause=2):
    #     result.append(i)
 
    # # displaying result
    # msg = response.message(f"--- Results for '{user_msg}' ---")
    # for result in search_results:
    #     msg = response.message(result)
 
    return send_message(response)