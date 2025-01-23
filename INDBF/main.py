import time
from zenoh import Config, open
import json

conf = Config()
conf.insert_json5("connect/endpoints", json.dumps(["tcp/127.0.0.1/7447"]))
session = open(conf)


key = 'data/raw'

def receive_data(sample):
    print(f'Received data: {sample.payload.decode()}')

sub = session.declare_subscriber(key, receive_data)

print(f'iNDBF ready to receive data on key: {key}')

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     print('Stopping iNDBF...')
#     sub.undeclare()
#     session.close()
