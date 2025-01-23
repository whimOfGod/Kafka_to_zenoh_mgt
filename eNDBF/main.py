import time
from zenoh import Config, open
import json

conf = Config()
conf.insert_json5("connect/endpoints", json.dumps(["tcp/127.0.0.1/7447"]))
session = open(conf)

key = 'data/preprocessed'

def receive_preprocessed_data(sample):
    print(f'Received preprocessed data: {sample.payload.decode()}')

sub = session.declare_subscriber(key, receive_preprocessed_data)

print(f'eNDBF ready to receive preprocessed data on key: {key}')

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     print('Stopping eNDBF...')
#     sub.undeclare()
#     session.close()
