# Используем базовый образ Python
FROM python:3.9-slim

# Указываем рабочую директорию
WORKDIR /model_api

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential python3-dev libffi-dev libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем код в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r req.txt

# Запускаем сервер при запуске контейнера
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

#docker build . -t andreyson
#docker run -p 8000:8000 -d --name name andreyson