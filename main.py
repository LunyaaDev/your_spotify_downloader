import os
from dotenv import load_dotenv
import pymongo
import subprocess
import time

load_dotenv()


mongodb_url = os.environ.get("MONGODB_URL")
mongodb_database = os.environ.get("MONGODB_DATABASE", "your_spotify")
download_dir = os.environ.get("DOWNLOAD_DIR", "/download")

# Init MongoDB
client = pymongo.MongoClient(mongodb_url)
database = client[mongodb_database]
tracks_collection = database["tracks"]

# run forever
while 1:
    # Get tracks from database
    tracks = [track for track in tracks_collection.find()]

    # get list of downloaded track ids
    existing_files = os.listdir(download_dir)
    existing_ids = [x.replace(".mp3", "") for x in existing_files]

    # filter non downloaded tracks
    tracks_to_download = [track for track in tracks if track["id"] not in existing_ids]

    # download tracks using spotdl
    for track in tracks_to_download:
        subprocess.run(
            [
                "spotdl",
                "--output",
                os.path.join(download_dir, "{track-id}.{output-ext}"),
                track["external_urls"]["spotify"],
            ]
        )

    # wait 10 min and rerun
    time.sleep(60 * 10)
