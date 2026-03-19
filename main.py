from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Serve frontend
@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/script.js")
def js():
    return FileResponse("static/script.js")

# Prediction API
@app.post("/predict")
async def predict(data: dict):
    text = data.get("text", "")
    prediction = model.predict([text])[0]
    return {"prediction": prediction}
