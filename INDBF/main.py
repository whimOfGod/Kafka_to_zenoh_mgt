import zenoh
import time

# Initialisation Zenoh
session = zenoh.open({"connect": "tcp/zenoh_broker:7447"}) # Connexion au broker Zenoh
key = 'data/raw'

def receive_data(sample):
    print(f'Received data: {sample.payload.decode()}')

# Créer un souscripteur
sub = session.declare_subscriber(key, receive_data)

print(f'iNDBF ready to receive data on key: {key}')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Stopping iNDBF...')
    sub.undeclare()
    session.close()
