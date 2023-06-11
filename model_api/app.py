from fastapi import FastAPI
import pandas as pd
import pickle
from sklearn.linear_model import SGDRegressor


app = FastAPI(debug=True)

@app.post('/predict')
async def predict(data):
    with open('pickle_model.pkl', 'rb') as file: 
        model: SGDRegressor = pickle.load(file)
        return model.predict(data)