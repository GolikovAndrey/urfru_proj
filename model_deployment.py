import pickle
import pandas as pd
import streamlit as st
from sklearn.metrics import r2_score

import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

list_files('/')

val = pd.read_csv('/temp_data/val.csv')
y_val = pd.read_csv('/temp_data/y_val.csv')

with open('pickle_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Streamlit приложение для предсказания")
st.write("Здесь вы можете запустить предсказание по кнопке и получить метрику R2 и таблицу с данными val.")

if st.button("Запустить предсказание"):
    predict = model.predict(val)

    r2 = r2_score(y_val, predict)
    st.write(f"R2 score: {r2:.2f}")

    val['Predicted'] = predict
    st.write("Таблица с данными val и предсказаниями:")
    st.write(val)