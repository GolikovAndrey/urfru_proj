import pickle
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import SGDRegressor

val = pd.read_csv('temp_data/val.csv')
y_val = pd.read_csv('temp_data/y_val.csv')

with open('model/pickle_model.pkl', 'rb') as file: 
    model = pickle.load(file)


predict = model.predict(val)

print(r2_score(y_val, predict))