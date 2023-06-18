# Используйте официальный образ Python 3.9
FROM python:3.9-slim

# Задайте рабочую директорию
WORKDIR /urfu_proj

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential python3-dev libffi-dev libssl-dev curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Скопируйте файлы проекта
COPY req.txt req.txt

# Установите зависимости Python
RUN pip install --no-cache-dir -r req.txt

# Скопируйте оставшиеся файлы проекта
COPY /model_deployment.py model_deployment.py
COPY /temp_data temp_data

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "model_deployment.py", "--server.port=8501", "--server.address=0.0.0.0"]