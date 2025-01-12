# Dockerfile pour le service FL Server
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y git curl && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    export PATH="$HOME/.cargo/bin:$PATH" && \
    rustup default stable && \
    rustup update && \
    apt-get clean

ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app
COPY ./server_driver.py /app
COPY /requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "server_driver.py"]
