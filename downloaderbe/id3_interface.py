from downloaderbe.song_metadata import SongMetadataLite
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC, TXXX, TYER, TLEN, TPE2, TRCK, TCON


def write_id3_tags(metadata: SongMetadataLite, mp3_path: str):
    """
    Commits the metadata to the mp3 file at the given path.
    """

    tags = ID3()
    tags[TIT2] = TIT2(encoding=3, text=metadata.title)
    tags[TPE1] = TPE1(encoding=3, text=metadata.artist)
    tags[TALB] = TALB(encoding=3, text=metadata.album)
    tags[TPE2] = TPE2(encoding=3, text=metadata.album_artist)
    tags[TRCK] = TRCK(encoding=3, text=str(metadata.track_num))
    tags[TYER] = TYER(encoding=3, text=metadata.release_year)
    tags[TLEN] = TLEN(encoding=3, text=str(metadata.length))
    tags[TCON] = TCON(encoding=3, text="/".join(metadata.genres))
    tags[APIC] = APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=metadata.album_art)
    tags[TXXX] = TXXX(encoding=3, desc="Recording ID", text=metadata.recording_id)
    tags[TXXX] = TXXX(encoding=3, desc="Release ID", text=metadata.release_id)
    tags.save(mp3_path, v2_version=3)
