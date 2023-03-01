import pandas as pd
from sklearn.model_selection import train_test_split

train = pd.read_csv(
    'data\dataset.csv', 
    delimiter = ',', 
    index_col = 'index'
)

X_train, X_val, y_train, y_val = train_test_split(train[['year', 'code', 'id']], train[['polution']], test_size = 0.3, random_state = 42)

X_train.to_csv('temp_data\X_train.csv')
X_val.to_csv('temp_data\X_val.csv')
y_train.to_csv('temp_data\y_train.csv')
y_val.to_csv('temp_data\y_val.csv')