# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

# Enable CORS so front-end can call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your front-end URL if deployed
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running."}

@app.post("/predict")
async def predict(data: dict):
    text = data.get("text", "")
    prediction = model.predict([text])[0]
    return {"prediction": prediction}