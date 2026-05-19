from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

app = FastAPI()

model = joblib.load("depression_model.pkl")


class UserData(BaseModel):
    age: int
    gender: int
    daily_social_media_hours: float
    platform_usage: int
    sleep_hours: float
    screen_time_before_sleep: float
    academic_performance: float
    physical_activity: float
    social_interaction_level: int
    stress_level: int
    anxiety_level: int
    addiction_level: int

@app.get("/")
def home():
    return {"message": "Welcome to the Depression Prediction API!"}

@app.post("/predict")
def predict_depression(data: UserData):
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    return {"depression_risk": int(prediction[0])}

