# Dockerfile pour le service FL Inference
FROM python:3.9-slim


WORKDIR /app
COPY ./anomaly_detection.py /app
COPY /requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "anomaly_detection.py"]
