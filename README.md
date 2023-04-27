Steps to run the app:

1. Install dependencies: poetry install
2. Get into poetry shell: poetry shell
3. Run app locally:  uvicorn app.main:app --reload  
4. Run server exposed to internet with ngrok:  ngrok http 8000