import zenoh
import json
import time

session = zenoh.open({"connect": "tcp/zenoh_broker:7447"}) # Connexion au broker Zenoh
input_key = 'data/preprocessed'

threshold = 0.5

# Fonction d'inférence basique pour la détection d'anomalies
def inference(sample):
    try:
        data = json.loads(sample.payload.decode())
        anomaly_detected = any(value > threshold for value in data.values())
        status = "Anomaly Detected" if anomaly_detected else "Normal"
        print(f"Inference Result: {status}")
    except Exception as e:
        print(f"Error during inference: {e}")

sub = session.declare_subscriber(input_key, inference)

print(f'FL Inference Agent ready to detect anomalies on key: {input_key}')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Stopping FL Inference Agent...')
    sub.undeclare()
    session.close()
