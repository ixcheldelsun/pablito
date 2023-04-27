Steps to run the app:

Install dependencies: poetry install
Get into poetry shell: poetry shell
Run app locally:  uvicorn app.main:app --reload  
Run server exposed to internet with ngrok:  ngrok http 8000