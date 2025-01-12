import zenoh
import time

# Initialisation Zenoh
session = zenoh.open({"connect": "tcp/zenoh_broker:7447"}) # Connexion au broker Zenoh
key = 'data/preprocessed'

def receive_preprocessed_data(sample):
    print(f'Received preprocessed data: {sample.payload.decode()}')

# Créer un souscripteur
sub = session.declare_subscriber(key, receive_preprocessed_data)

print(f'eNDBF ready to receive preprocessed data on key: {key}')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Stopping eNDBF...')
    sub.undeclare()
    session.close()
