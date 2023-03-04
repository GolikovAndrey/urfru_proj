@REM Разделение данных на обучающую и валидационную выборки, обработка данных

mkdir temp_data
python data_creation.py 
python data_preprocessing.py

@REM Обучение модели и валидация результатов
python model_learning.py
python model_deployment.py

rmdir /s /q temp_data
pause