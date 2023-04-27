from twilio.rest import Client
from dotenv import load_dotenv
import os
import re
from app.agents.agent import EventAgent
from config import logger

load_dotenv()


class Chatbot:
    
    def __init__(self):
        self.number = os.environ['TWILIO_NUMBER']
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.client = Client(self.account_sid, self.auth_token)
        self.event_agent = EventAgent()
        
        
    def send_message(self, body_text, to_number=None):
        logger.info("Sending message {message} to number {to_number}".format(message=body_text, to_number=to_number))
        number = '+' + str(re.findall(r'\d+', to_number)[0])
        try:
            self.client.messages.create(
                from_=F"whatsapp:{self.number}", body=body_text, to=f"whatsapp:{number}"
            )
        except Exception as e:
            logger.error("Error sending message: {error}".format(error=str(e)))
            self.client.messages.create(
                from_=F"whatsapp:{self.number}", body="Un error ha ocurrido. Regrese más tarde.", to=f"whatsapp:{number}"
            )
        
    
    def run(self, message, sender) -> None:
        response = self.event_agent.conversation_chat(message)
        try:
            self.send_message(response, sender)
        except Exception as e:
            logger.error(str(e))
        
        

chatbot = Chatbot()