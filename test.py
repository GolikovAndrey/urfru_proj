import pytest
import pandas as pd
import os
import pickle
import numpy as np
from sklearn.metrics import r2_score




paths_to_datasets = []
for file in os.listdir("data/"):
    if file.endswith(".csv"):
        paths_to_datasets.append(os.path.join("data/", file))

@pytest.mark.parametrize('path_to_dataset', paths_to_datasets)
def test_dataset(path_to_dataset):
    data = pd.read_csv(path_to_dataset)
    model = pickle.load(open('model/model.pkl', 'rb'))
    predictions= model.predict(data[['x']])
    r2=r2_score((data[['y']]), predictions)
    print(r2)
    assert r2 >= 0.6, f"Датасет {path_to_dataset} не прошел проверку по метрике."
