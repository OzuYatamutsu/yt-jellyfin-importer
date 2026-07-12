from requests import get


def resolve_release_id(recording_id: str) -> str:
    """
    Resolves the release id of the given recording id.
    """

    url = f"https://musicbrainz.org/ws/2/recording/{recording_id}?inc=releases&fmt=json"
    response = get(url)
    response.raise_for_status()
    data = response.json()

    if "releases" in data and len(data["releases"]) > 0:
        return data["releases"][0]["id"]
    else:
        raise ValueError(f"No releases found for recording id {recording_id}")
