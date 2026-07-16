from downloaderbe.song_metadata import SongMetadataLite
from pathlib import Path
from shutil import move
import downloaderbe.config as config


def move_file_to_jellyfin_dir(metadata: SongMetadataLite) -> None:
    original_path = f"{config.OUTPUT_LOCATION}/{metadata.artist} - {metadata.title}.mp3"
    target_path = Path(
        config.JELLYFIN_LIBRARY
        + f"/{metadata.album_artist}"
        + f"/{metadata.album}"
    )
    target_path.mkdir(
        parents=True, exist_ok=True
    )
    move(
        original_path,
        f"{target_path.name}/{metadata.artist} - {metadata.title}.mp3"
    )
