import pickle
import pandas as pd
from sklearn.metrics import r2_score

val = pd.read_csv('temp_data/val.csv')
y_val = pd.read_csv('temp_data/y_val.csv')

with open('pickle_model.pkl', 'rb') as file: 
    model = pickle.load(file)


predict = model.predict(val)

print(f'r2 score: {r2_score(y_val, predict)}')