@REM Создание папки, в которую будет скачиваться датасет из Google Drive, и временной папки

mkdir data
mkdir temp_data

@REM Разделение данных на обучающую и валидационную выборки и обработка выборок

python data_creation.py 
python data_preprocessing.py

@REM Обучение модели и валидация результатов
python model_learning.py
python model_deployment.py

rmdir /s /q temp_data
pause