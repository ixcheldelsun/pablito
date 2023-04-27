import os
from dotenv import load_dotenv
from twilio.rest import Client
from fastapi import FastAPI, Form, Body, Request
import uvicorn
import re

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

app = FastAPI(debug=True)


def send_message(body_text, to_number=None):
    number = '+' + str(re.findall(r'\d+', to_number)[0])
    client.messages.create(
        from_="whatsapp:+14155238886", body=body_text, to=f"whatsapp:{number}"
    )


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/message")
async def init_bot(From: str = Form(...), Body: str = Form(...) ):
    response = f"Hello, I am a bot. I am still learning. I got the following message from you: {str(Body)}."

    return send_message(response, From)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)