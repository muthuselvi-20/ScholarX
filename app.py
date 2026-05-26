from fastapi import FastAPI
from matplotlib.pylab import float64, int64
from pydantic import BaseModel
import joblib
import pandas as pd
from validate import validation

app = FastAPI()

model = joblib.load("depression_model.pkl")

class user_input(BaseModel):
    age: int
    gender: int
    daily_social_media_hours: float
    platform_usage: int
    sleep_hours: float
    screen_time_before_sleep: float
    academic_performance:float
    physical_activity:float
    social_interaction_level:int
    stress_level:int
    anxiety_level:int
    addiction_level:int

@app.get("/")
def root():
    return {"message": "Welcome to the Depression Prediction API!"}

@app.post("/predict")
def predict(input: user_input):
    input_data = pd.DataFrame([input.dict()])
    errors = validation(input_data)
    if errors:
        return {"errors": errors}
    
    prediction = model.predict(input_data)[0]
    result = "Depression Detected" if prediction == 1 else "No Depression"

    return {"prediction": result}
    
