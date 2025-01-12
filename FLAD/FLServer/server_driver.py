import zenoh
import json

session = zenoh.open({"connect": "tcp/zenoh_broker:7447"}) # Connexion au broker Zenoh
input_key = 'data/preprocessed'

aggregated_results = []

def aggregate_results(sample):
    try:
        data = json.loads(sample.payload.decode())
        aggregated_results.append(data)
        print(f"Aggregated Data: {aggregated_results}")
        # Calculer la moyenne des valeurs collectées
        avg_result = sum([sum(d.values()) for d in aggregated_results]) / len(aggregated_results)
        print(f"Global Model Value: {avg_result}")
    except Exception as e:
        print(f"Error during aggregation: {e}")

sub = session.declare_subscriber(input_key, aggregate_results)

print(f'FL Server ready to aggregate data from key: {input_key}')

try:
    while True:
        pass
except KeyboardInterrupt:
    print('Stopping FL Server...')
    sub.undeclare()
    session.close()
