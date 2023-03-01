import pickle
import pandas as pd
from sklearn.linear_model import SGDRegressor


train = pd.read_csv(
    'temp_data/train.csv',
    delimiter = ','
)


y_train = pd.read_csv(
    'temp_data/y_train.csv',
    delimiter = ',', 
    index_col = 'index'
)


regr = SGDRegressor()


regr.fit(train, y_train)

pkl_filename = 'model/pickle_model.pkl'

with open(pkl_filename, 'wb') as file: 
    pickle.dump(regr, file) 