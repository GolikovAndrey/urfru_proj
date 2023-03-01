import pickle
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error


val = pd.read_csv('temp_data/val.csv')
y_val = pd.read_csv('temp_data/y_val.csv')


with open('model/pickle_model.pkl', 'rb') as file: 
    model = pickle.load(file)


predict = model.predict(val)

print(mean_squared_error(y_val, predict))
# print(r2_score(y_val, pd.DataFrame(predict)))