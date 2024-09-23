from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

model = joblib.load('svm_model.joblib')

app = FastAPI()

class model_input(BaseModel):

    f1 : float
    f2 : float
    f3 : float
    f4 : float

@app.post('/predict')
def predict(input_data : model_input):
    input_array = np.array([[input_data.f1,input_data.f2,input_data.f3,input_data.f4]])
    prediction = model.predict(input_array)
    return {'prediction': prediction.tolist()[0]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port = 8000)