import pickle
import pandas as pd
with open('model/model.pkl','rb')as f:
    model=pickle.load(f)
    
model_version="1.0.0"
model_classes=model.classes_.tolist()
def predict_data(data_point:dict):
    data_frame=pd.DataFrame([data_point])
    response=model.predict(data_frame)[0]
    probabilities=model.predict_proba(data_frame)[0]
    current_class_prob=max(probabilities)
    allprobs=dict(zip(model_classes,map(lambda x:round(x,4),probabilities)))
    return {
        "response":response,
        "response_confidence":current_class_prob,
        "all_class_probs":allprobs
    }
    
    
    
    