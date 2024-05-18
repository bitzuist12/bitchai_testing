import nomic
from nomic import AtlasDataset
import time

def fetch_map():
    attempts = 0
    while attempts < 5:
        try:
            map = AtlasDataset('cs-collection').maps[0]
            return map
        except Exception as e:
            print(f"Attempt {attempts + 1}: {str(e)}")
            time.sleep(5)  # wait for 5 seconds before retrying
            attempts += 1
    raise Exception("Failed to fetch map after several attempts.")

map = fetch_map()