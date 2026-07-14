from song_metadata import SongMetadataLite
from acoustid import match
import config


def resolve_audio_fp(path_to_mp3: str) -> SongMetadataLite:
    """
    Resolves the audio fingerprint of the given mp3 file and returns metadata
    for further querying.
    """

    for _, recording_id, title, artist in match(
        config.ACOUSTID_API_KEY,
        path_to_mp3
    ):
        return SongMetadataLite(
            title=title,
            artist=artist,
            album="",
            album_artist="",
            genres=[],
            track_num=0,
            recording_id=recording_id,
            release_id="",
            release_year="",
            album_art=b"",
            length=0
        )
