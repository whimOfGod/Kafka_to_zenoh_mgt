import time
import json
from zenoh import Config, open


conf = Config()
import json
conf.insert_json5("connect", json.dumps({"endpoints": ["tcp/zenoh_broker:7447"]}))

session = open(conf)

input_key = 'data/raw'

# Simulated FL Client Training Function
def train_on_data(sample):
    try:
        data = json.loads(sample.payload.decode())
        print(f"Training on data: {data}")
        trained_value = sum(data.values()) / len(data)
        print(f"Trained Value: {trained_value}")
    except Exception as e:
        print(f"Error during training: {e}")

sub = session.declare_subscriber(input_key, train_on_data)

print(f'FL Client ready to train on data from key: {input_key}')

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     print('Stopping FL Client...')
#     sub.undeclare()
#     session.close()
