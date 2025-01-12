# Dockerfile pour le service eNDBF
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y git cargo rustc && \
    apt-get clean

WORKDIR /app
COPY ./main.py /app
COPY /requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
