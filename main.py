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

    # download tracks using spotdl
    for track in tracks:
        subprocess.run(
            [
                "spotdl",
                "--output",
                os.path.join(download_dir, "{artist}/{artists} - {title}.{output-ext}"),
                track["external_urls"]["spotify"],
            ]
        )

    # wait 10 min and rerun
    time.sleep(60 * 10)
