from google.cloud import bigquery

client = bigquery.Client(
    project="studied-slate-499209-e8"
)

datasets = list(client.list_datasets())

print("\nConnected Successfully!\n")

for dataset in datasets:
    print(dataset.dataset_id)