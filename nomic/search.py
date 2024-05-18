from nomic import atlas
import pandas
import numpy as np
from nomic import embed
import numpy as np

dataset = atlas.map_data(data="cs-collection", indexed_field='text')

map = dataset.maps[0]

# Run vector search on your map for points with ID numbers 100, 111, 112
# neighbors, distances = map.embeddings.vector_search(ids=[100,111,112], k=5)

output = embed.text(
    texts=['The text you want to embed.'],
    model='nomic-embed-text-v1.5',
    task_type='search_document', #OR search_query
)

embeddings = np.array(output['embeddings'])




random_query_vector = np.random.rand(1, 768)

#BURADA KENDIM BIR CIKARTIRSAM QUERY VECTORU...

# Searches for k-nearest neighbors of random_query_vector
with dataset.wait_for_dataset_lock():
    neighbors, distances = map.embeddings.vector_search(queries=random_query_vector, k=10)

print("Neighbor IDs:", neighbors)

data = dataset.get_data(ids=query_document_ids)
for datum, datum_neighbors in zip(data, neighbors):
    neighbor_data = dataset.get_data(ids=datum_neighbors)
    print(f"The ten nearest neighbors to the query point {datum} are {neighbor_data}")


neighbors, distances = map[0].embeddings.vector_search(ids=[100,111,112], k=5)


#####


def embed_query(query: str):
    query = np.array(
        embed.text(
            [query],
            model="nomic-embed-text-v1.5",
            task_type="search_query",
        )["embeddings"]
    )[0]
    return query


test_query = embed_query("tree data structures")
test_query.shape

def knn_scan(query, k=10): return np.argsort(query @ wiki100k_embeddings.T)[-k:]

full_top10 = knn_scan(test_query)
[doc[:100] for doc in wiki100k[full_top10]['text']]
