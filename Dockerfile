FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY producer.py consumer.py ./

CMD ["python", "-c", "print('Kafka Python application image built successfully')"]
