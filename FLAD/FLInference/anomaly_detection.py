import time
import json

from zenoh import Config, open

conf = Config()
conf.insert_json5("connect", json.dumps({"endpoints": ["tcp/zenoh_broker:7447"]}))
session = open(conf)

input_key = 'data/preprocessed'
threshold = 0.5

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

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     print('Stopping FL Inference Agent...')
#     sub.undeclare()
#     session.close()
