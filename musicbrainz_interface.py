from config import DOWNLOAD_LOCATION
from requests import get


def resolve_release(recording_id: str) -> str:
    """
    Resolves the album name and release id of the given recording id.
    """

    url = f"https://musicbrainz.org/ws/2/recording/{recording_id}?inc=releases&fmt=json"
    response = get(url)
    response.raise_for_status()
    data = response.json()

    if "releases" in data and len(data["releases"]) > 0:
        return data["releases"][0]["title"], data["releases"][0]["id"]
    else:
        raise ValueError(f"No releases found for recording id {recording_id}")


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
