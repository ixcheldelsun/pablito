from twilio.rest import Client
from dotenv import load_dotenv
import os
import re


load_dotenv()


class Chatbot:
    
    def __init__(self):
        self.number = os.environ['TWILIO_NUMBER']
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.client = Client(self.account_sid, self.auth_token)
        
    def send_message(self, body_text, to_number=None):
        number = '+' + str(re.findall(r'\d+', to_number)[0])
        self.client.messages.create(
            from_=F"whatsapp:{self.number}", body=body_text, to=f"whatsapp:{number}"
        )
        

chatbot = Chatbot()