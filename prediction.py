import requests
import pandas as pd
import sys




to_predict = sys.argv[1]

headers = {
    "Content-Type": 'application/json'
}

json = {
    "data": to_predict
}

requests.post(url="127.0.0.1:8000/predict", headers=headers, json=json)