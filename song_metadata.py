from dataclasses import dataclass

@dataclass
class SongMetadataLite:
    """
    Contains specifically the metadata relevant for querying for further metadata."""

    title: str
    artist: str
    album: str
    recording_id: str
    release_id: str
