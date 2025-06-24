# download_data.py
import os

# Make sure you installed kaggle: pip install kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

DATASET = "irkaal/foodcom-recipes-and-reviews"

# Destination folder
DEST = "data"

os.makedirs(DEST, exist_ok=True)

api = KaggleApi()
api.authenticate()

print(f"Downloading {DATASET}...")
api.dataset_download_files(DATASET, path=DEST, unzip=True)

print(f"Download complete! Files saved to {DEST}/")
