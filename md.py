from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json

app = FastAPI()

class model_input(BaseModel):

    Pregnancies : int
    Glucose: int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

diabetes_model = joblib.load('model.joblib')

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin= input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg,glu,bp,skin,insulin,bmi,dpf,age]



    prediction = diabetes_model.predict([input_list])

    if prediction[0] ==0:
        return 'Not Diabetic'
    else:
        return 'Diabetic'




