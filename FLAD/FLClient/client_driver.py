import zenoh
import json
import time

session = zenoh.open({"connect": "tcp/zenoh_broker:7447"}) # Connexion au broker Zenoh
input_key = 'data/preprocessed'

# Simulated FL Client Training Function
def train_on_data(sample):
    try:
        data = json.loads(sample.payload.decode())
        print(f"Training on data: {data}")
        # Simuler un simple entraînement (moyenne des valeurs)
        trained_value = sum(data.values()) / len(data)
        print(f"Trained Value: {trained_value}")
    except Exception as e:
        print(f"Error during training: {e}")

sub = session.declare_subscriber(input_key, train_on_data)

print(f'FL Client ready to train on data from key: {input_key}')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Stopping FL Client...')
    sub.undeclare()
    session.close()
