# yt-jellyfin-importer
Given a YouTube link, downloads an MP3 to the specified directory and populates with metadata.

Contains both a command line script and a django web application.

## Usage (command line script)
```
python downloaderbe/main.py <youtube_link> --acoustid-api-key <api-key> [--output-location <output-location>] [--jellyfin-library <path-to-jellyfin-music-library>]
```

To run, get an Acoustid API key [here](https://acoustid.org/new-application).

## Usage (django)
```
source .venv/activate
JELLYFIN_LIBRARY=<path-to-jellyfin-music-library> ACOUSID_API_KEY=<api-key> python mange.py runserver [portnum]
```

