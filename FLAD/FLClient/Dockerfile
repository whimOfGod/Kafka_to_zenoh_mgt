# Dockerfile pour le service FL Client
FROM python:3.9-slim

WORKDIR /app
COPY ./client_driver.py /app
COPY /requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "client_driver.py"]
