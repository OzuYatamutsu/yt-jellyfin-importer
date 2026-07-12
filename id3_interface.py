from song_metadata import SongMetadataLite
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC, TXXX, TORY, TLEN


def write_id3_tags(metadata: SongMetadataLite, mp3_path: str):
    """
    Commits the metadata to the mp3 file at the given path.
    """

    tags = ID3(mp3_path)
    tags.add(TIT2(encoding=3, text=metadata.title))
    tags.add(TPE1(encoding=3, text=metadata.artist))
    tags.add(TALB(encoding=3, text=metadata.album))
    tags.add(TORY(encoding=3, text=metadata.release_year))
    tags.add(TLEN(encoding=3, text=str(metadata.length)))
    tags.add(APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=metadata.album_art))
    tags.add(TXXX(encoding=3, desc="Recording ID", text=metadata.recording_id))
    tags.add(TXXX(encoding=3, desc="Release ID", text=metadata.release_id))
    tags.save(mp3_path)
