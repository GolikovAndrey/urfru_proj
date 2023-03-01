import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

train = pd.read_csv(
    'temp_data\X_train.csv',
    delimiter = ',', 
    index_col = 'index'
)

val = pd.read_csv(
    'temp_data\X_val.csv', 
    delimiter = ',', 
    index_col = 'index'
)


cat_col = [col_name for col_name in train.columns if train[col_name].dtypes == object]
num_col = [col_name for col_name in train.columns if train[col_name].dtypes != object]


encoder = OneHotEncoder(drop='first', handle_unknown='ignore', sparse=False)
min_max_scaler = MinMaxScaler()


train_cat = encoder.fit_transform(train[cat_col])
val_cat = encoder.transform(val[cat_col])


train_cat = pd.DataFrame(train_cat)
val_cat = pd.DataFrame(val_cat)


train_norm = min_max_scaler.fit_transform(train[num_col])
val_norm = min_max_scaler.transform(val[num_col])


train_norm = pd.DataFrame(train_norm, columns=num_col)
val_norm = pd.DataFrame(val_norm, columns=num_col)


train = train_cat.join(train_norm)
val = val_cat.join(val_norm)


train.to_csv('temp_data/train.csv')
val.to_csv('temp_data/val.csv')