# Используем базовый образ Python
FROM python:3.12-alpine

# Устанавливаем зависимости
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем исходный код приложения в контейнер
COPY . /app
WORKDIR /app

# Запускаем приложение
CMD ["python", "app.py"]
