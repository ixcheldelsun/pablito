from dotenv import load_dotenv
from fastapi import FastAPI, Form
import uvicorn
from app.models.chatbot import chatbot


load_dotenv()

app = FastAPI(debug=True)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/message")
async def init_bot(From: str = Form(...), Body: str = Form(...) ):
    response = f"Hello, I am a bot. I am still learning. I got the following message from you: {str(Body)}."
    return chatbot.send_message(response, From)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)