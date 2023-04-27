from dotenv import load_dotenv
from fastapi import FastAPI, Form
import uvicorn
from app.models.chatbot import chatbot
from config import logger

load_dotenv()

app = FastAPI(debug=True)


@app.get("/")
def root():
    return {"message": "Hello World"}



@app.post("/message")
async def bot(From: str = Form(...), Body: str = Form(...)):
    logger.info(f"Received message from {From}: {Body}")
    return chatbot.run(Body, From)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)