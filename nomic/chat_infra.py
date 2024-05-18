import nomic
from nomic import AtlasDataset, embed
from nomic import atlas
import numpy as np
# Load a dataset from the 'cs-collection'
dataset = AtlasDataset('cs-collection')
print("Dataset loaded successfully.")  # Debug: Confirm dataset load

map = dataset.maps[0]
print("Map accessed from dataset.")  # Debug: Confirm map access

# Access various properties of the map
print("Map Topics:", map.topics)  # Debug: Print topics
print("Map Embeddings:", map.embeddings)  # Debug: Print embeddings
print("Map Data:", map.data)  # Debug: Print data

# Retrieve different types of embeddings
# projected_embeddings = map.embeddings.projected
# latent_embeddings = map.embeddings.latent

def embed_query(query: str):
    # Convert the text query into an embedding using the specified model
    print(f"Embedding query: {query}")  # Debug: Show the query being embedded
    query_embedding = np.array(
        embed.text(
            [query],
            model="nomic-embed-text-v1.5",
            task_type="search_query", 
        )["embeddings"]
    )[0]
    print(f"Query embedding shape: {query_embedding.shape}")  # Debug: Print shape of the embedding
    return query_embedding

# Embed a specific query and reshape for vector search
test_query = embed_query("Singapore cold storage market")
test_query = test_query.reshape(1, -1)
print("Test query reshaped for vector search.")  # Debug: Confirm reshaping

# Lock the dataset to ensure thread-safe operations
with dataset.wait_for_dataset_lock():
    print("Dataset lock acquired.")  # Debug: Confirm lock acquisition
    # Perform a vector search to find the top 10 nearest neighbors
    neighbors, distances = map.embeddings.vector_search(queries=test_query, k=10)
    print("Vector search completed.")  # Debug: Confirm search completion
    print("Neighbor IDs:", neighbors)  # Debug: Print the IDs of the nearest neighbors
    print("Distances:", distances)  # Debug: Print distances to neighbors

# Fetch data for the nearest neighbor
data = dataset.get_data(ids=neighbors[0])
print(f"Data fetched for neighbor ID {neighbors[0]}")  # Debug: Confirm data fetch
for i, point in enumerate(data):
    if i == 0:
        print('Initial point:', point, '\n')  # Debug: Print the initial point
        print('Nearest neighbors:')
    else:
        print(point)  # Debug: Print each of the nearest neighbors