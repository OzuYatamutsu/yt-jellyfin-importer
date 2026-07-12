from config import DOWNLOAD_LOCATION
from subprocess import run
from uuid import uuid4


def download_to_mp3(link: str) -> str:
    """
    Downloads a video from the given link and converts it to mp3 format using yt-dlp.

    Downloads to the directory specified in config.py.
    Returns the full path to the downloaded mp3 file.
    """

    output_id = uuid4()
    result = run([
        "yt-dlp",
        "--extract-audio", "--audio-format", "mp3",
        link,
        "-o", f"{DOWNLOAD_LOCATION}/{output_id}.mp3"
    ])

    return f"{DOWNLOAD_LOCATION}/{output_id}.mp3"
