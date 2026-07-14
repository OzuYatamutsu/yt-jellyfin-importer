from dataclasses import dataclass

@dataclass
class SongMetadataLite:
    """
    Contains specifically the metadata relevant for querying for further metadata."""

    title: str
    artist: str
    album: str
    album_artist: str
    genres: list[str]
    track_num: int
    recording_id: str
    release_id: str
    release_year: str
    album_art: bytes
    length: int = 0
