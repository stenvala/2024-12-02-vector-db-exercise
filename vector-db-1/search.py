from pathlib import Path
from pymilvus import MilvusClient
from pymilvus import model

collection = "finnish_cities"

dir = Path(__file__).parent.absolute() / collection

client = MilvusClient(f"{collection}.db")

embedding_fn = model.DefaultEmbeddingFunction()

query_vectors = embedding_fn.encode_queries(["Find small cities"])

res = client.search(
    collection_name=collection,  # target collection
    data=query_vectors,  # query vectors
    limit=4,  # number of returned entities
    output_fields=["text", "subject", "city"],  # specifies fields to be returned
)
print("-" * 100)
for i in res[0]:
    print("*" * 50)
    print(i["distance"], i["entity"]["city"])
    print(i["entity"]["text"])
