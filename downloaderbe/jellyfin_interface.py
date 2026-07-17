from downloaderbe.song_metadata import SongMetadataLite
from pathlib import Path
from shutil import move
import downloaderbe.config as config


def move_file_to_jellyfin_dir(metadata: SongMetadataLite) -> str:
    original_path = f"{config.OUTPUT_LOCATION}/{metadata.artist} - {metadata.title}.mp3"
    target_path = Path(
        config.JELLYFIN_LIBRARY
        + f"/{metadata.album_artist}"
        + f"/{metadata.album} ({metadata.release_year})"
    )
    target_path.mkdir(
        parents=True, exist_ok=True
    )
    target_path = f"{target_path.resolve()}/{metadata.artist} - {metadata.title}.mp3"
    move(original_path, target_path)
    return target_path
