from fastapi import FastAPI,Path,HTTPException, Query
import json
import pandas as pd
from fastapi.responses import JSONResponse
from schema.patient import patient
from model.loadmodel import predict_data,model_version,model
from schema.responsemodel import responsemodel

app=FastAPI()
@app.get("/")
def home():
    return {"message":"Insurance premium prediction api"}
@app.get("/health")
def health():
    return {
        "status":"ok",
        "version":model_version,
        "model_loaded": model is not None
    }
@app.post("/predict",response_model=responsemodel,status_code=201)
def predict_premium(data:patient):
    data_point={
        "income_lpa":data.income_lpa,
        "occupation":data.occupation,
        "bmi":data.bmi,
        "agegroup":data.agegroup,
        "lifestylerisk":data.lifestylerisk,
        "city_tier":data.city_tier
        
    }
    try:
        response=predict_data(data_point)
        return response
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
    