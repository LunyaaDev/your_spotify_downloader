# your_spotify downloader

An automated downloader for all tracks stored in [your_spotify](https://github.com/Yooooomi/your_spotify)

## Usage

### Running in Docker

```sh
docker run -d \
  -e MONGODB_URL=mongodb://localhost:27017 \
  -v "$(pwd)/download:/download" \
  lunyaadev/your_spotify_downloader
```

This will download all stored tracks from your_spotify into the `./download` directory.

## Environment variables

| Variable           | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| `MONGODB_URL`      | URL of the MongoDB                                              |
| `MONGODB_DATABASE` | Name of the Database (defaults to `your_spotify`)               |
| `DOWNLOAD_DIR`     | Directory to download the tracks into (defaults to `/download`) |
| `BATCH_SIZE`       | Size of Track Batches for SpotDL (defaults to 100)              |
