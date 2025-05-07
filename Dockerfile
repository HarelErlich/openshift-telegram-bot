# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY bot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot/ .

ENV FLASK_ENV=production

CMD ["python", "app.py"]

