from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
import uvicorn
from app.models.chatbot import chatbot
from config import logger
from app.db import db
import json

load_dotenv()

app = FastAPI(debug=True)


@app.get("/")
def root():
    return {"message": "Hello World"}



@app.post("/message")
async def bot(From: str = Form(...), Body: str = Form(...)):
    logger.info(f"Received message from {From}: {Body}")
    return chatbot.run(Body, From)


@app.post("/webhook")
async def webhook(request:Request):
    import codecs
    import re
    
    data = await request.body()
    data = codecs.decode(data, "unicode_escape")
    
    logger.info(f"Received webhook: {data}")
    try:
        email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data)[-1:][0]
        await db.add_wedding({"data": data, "email": email})
    except Exception as e:
        logger.error(str(e))
        return {"error": str(e)}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", debug=True)