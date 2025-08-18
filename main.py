import os
from dotenv import load_dotenv
import pymongo
import subprocess
import time

load_dotenv()


def batch_list(items, batch_size=100):
    return [items[i : i + batch_size] for i in range(0, len(items), batch_size)]


mongodb_url = os.environ.get("MONGODB_URL")
mongodb_database = os.environ.get("MONGODB_DATABASE", "your_spotify")
download_dir = os.environ.get("DOWNLOAD_DIR", "/download")
batch_size = int(os.environ.get("BATCH_SIZE", "100"))

# Init MongoDB
client = pymongo.MongoClient(mongodb_url)
database = client[mongodb_database]
tracks_collection = database["tracks"]

# run forever
while 1:
    # Get tracks from database
    tracks = [track for track in tracks_collection.find()]

    # download tracks using spotdl
    for chunk in batch_list(tracks, batch_size):
        subprocess.run(
            [
                "spotdl",
                "--output",
                os.path.join(download_dir, "{artist}/{artists} - {title}.{output-ext}"),
                "download",
            ]
            + [track["external_urls"]["spotify"] for track in chunk]
        )
        print("waiting 1 min before continuing")
        time.sleep(60 * 1)
