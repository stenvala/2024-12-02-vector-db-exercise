from pathlib import Path
from pymilvus import MilvusClient
from pymilvus import model

collection = "finnish_cities"

dir = Path(__file__).parent.absolute() / collection

client = MilvusClient(f"{collection}.db")

if client.has_collection(collection_name=collection):
    client.drop_collection(collection_name=collection)
client.create_collection(collection_name=collection, dimension=768)

#

embedding_fn = model.DefaultEmbeddingFunction()

docs = []
for i in dir.glob("*.txt"):
    with open(i, "r") as f:
        # docs.append(f.read().split("\n")[0])
        docs.append({"data": f.read()[:2000], "city": i.stem})

print("There are", len(docs), "documents.")

vectors = embedding_fn.encode_documents([i["data"] for i in docs])

print("Dim:", embedding_fn.dim, vectors[0].shape)

# Each entity has id, vector representation, raw text, and a subject label that we use
# to demo metadata filtering later.
data = [
    {
        "id": i,
        "vector": vectors[i],
        "text": docs[i]["data"],
        "subject": "cities",
        "city": docs[i]["city"],
    }
    for i in range(len(vectors))
]

print("Data has", len(data), "entities, each with fields: ", data[0].keys())
print("Vector dim:", len(data[0]["vector"]))


res = client.insert(collection_name=collection, data=data)

print(res)
