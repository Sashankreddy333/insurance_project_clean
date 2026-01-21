from fastapi import FastAPI,Path,HTTPException, Query
import json
import pandas as pd
from fastapi.responses import JSONResponse
from schema.patient import patient
from model.loadmodel import model

app=FastAPI()

@app.post("/predict")
def predict_premium(data:patient):
    data_point=pd.DataFrame([{
        "income_lpa":data.income_lpa,
        "occupation":data.occupation,
        "bmi":data.bmi,
        "agegroup":data.agegroup,
        "lifestylerisk":data.lifestylerisk,
        "city_tier":data.city_tier
        
    }])
    response=model.predict(data_point)[0]
    return JSONResponse(status_code=201,content={"predicted_category":response })
    