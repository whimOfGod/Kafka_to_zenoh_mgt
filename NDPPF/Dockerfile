# Dockerfile pour le service NDPPF
FROM python:3.9-slim


WORKDIR /app
COPY ./preprocess.py /app
COPY /requirements.txt /app 

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "preprocess.py"]
