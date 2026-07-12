from song_metadata import SongMetadataLite
from config import DOWNLOAD_LOCATION
from requests import get


def resolve_release(recording_id: str, metadata: SongMetadataLite) -> SongMetadataLite:
    """
    Resolves the album name, release id, release year, and length of the given recording id.

    Adds this information to the SongMetadataLite object and returns it.
    """

    url = f"https://musicbrainz.org/ws/2/recording/{recording_id}?inc=releases+release-groups+artists+media+genres&fmt=json"
    response = get(url)
    response.raise_for_status()
    data = response.json()

    metadata.album = data["releases"][0]["title"]
    metadata.track_num = data["releases"][0]["media"][0]["tracks"][0]["number"]
    metadata.album_artist = data["artist-credit"][0]["artist"]["name"]
    metadata.release_id = data["releases"][0]["id"]
    metadata.release_year = data["first-release-date"]
    metadata.genres = [genre["name"] for genre in data.get("genres", [])]
    metadata.length = data["length"]

    return metadata

def get_cover_art_url(release_id: str) -> str:
    """
    Returns the cover art url for the given release id.
    """

    return f"https://coverartarchive.org/release/{release_id}/front"


def download_cover_art(release_id: str) -> bytes:
    """
    Downloads the cover art for the given release id and returns
    the raw bytes of the image.
    """

    url = get_cover_art_url(release_id)
    response = get(url)
    response.raise_for_status()

    return response.content
