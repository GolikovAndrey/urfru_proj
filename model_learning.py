import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score

train = pd.read_csv('temp_data/train.csv')

y_train = pd.read_csv('temp_data/y_train.csv')

regr = SGDRegressor(tol=.00001, eta0=.1)

regr.fit(train, np.ravel(y_train[['polution']]))
predict = regr.predict(train)
pkl_filename = 'pickle_model.pkl'

with open(pkl_filename, 'wb') as file:
    pickle.dump(regr, file)