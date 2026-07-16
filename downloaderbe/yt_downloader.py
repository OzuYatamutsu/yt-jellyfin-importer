from subprocess import run
from uuid import uuid4
import downloaderbe.config as config


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
        "-o", f"{config.DOWNLOAD_LOCATION}/{output_id}.mp3"
    ])

    return f"{config.DOWNLOAD_LOCATION}/{output_id}.mp3"
