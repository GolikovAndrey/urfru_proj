#!/bin/bash

#Создание папки, в которую будет скачиваться датасет из Google Drive, и временной папки

mkdir data
mkdir temp_data

#Разделение данных на обучающую и валидационную выборки и обработка выборок
pip install gdown
pip install scikit-learn
pip install pandas
python3 data_creation.py 
python3 data_preprocessing.py

#Обучение модели и валидация результатов
python3 model_learning.py
python3 model_deployment.py

rm -R temp_data
exit 0
