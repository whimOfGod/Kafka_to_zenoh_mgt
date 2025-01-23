import time
import json

from zenoh import Config, open

conf = Config()
conf.insert_json5("connect", json.dumps({"endpoints": ["tcp/zenoh_broker:7447"]}))

session = open(conf)

input_key = 'data/raw'
output_key = 'data/preprocessed'

def preprocess_data(sample):
    try:
        data = json.loads(sample.payload.decode())
        if 'value' in data:
            data['value'] = data['value'] / 100.0
            print(f"Preprocessed data: {data}")
            session.put(output_key, json.dumps(data))
    except Exception as e:
        print(f"Error in preprocessing: {e}")

sub = session.declare_subscriber(input_key, preprocess_data)

print(f'NDPPF ready to preprocess data on key: {input_key}')

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     print('Stopping NDPPF...')
#     sub.undeclare()
#     session.close()
