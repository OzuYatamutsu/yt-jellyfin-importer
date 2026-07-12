from yt_downloader import download_to_mp3
from acoustid_interface import resolve_audio_fp
from musicbrainz_interface import resolve_release, download_cover_art
from id3_interface import write_id3_tags


def main(youtube_link: str):
    print("[1/4] Downloading and converting to mp3...")
    mp3_path = download_to_mp3(youtube_link)
    print(f"Downloaded to {mp3_path}")
    print("[2/4] Generating audio fingerprint and resolving initial metadata...")
    metadata = resolve_audio_fp(mp3_path)
    print(f"Audio fingerprint and metadata resolved: {metadata}")
    print("[3/4] Resolving release id...")
    album_name, release_id = resolve_release(metadata.recording_id)
    metadata.release_id = release_id
    print(f"Release id resolved: {release_id}")
    print("[4/4] Downloading cover art...")
    metadata.album_art = download_cover_art(release_id)
    print(f"Cover art downloaded: {len(metadata.album_art)} bytes")
    print("[5/5] Writing ID3 tags...")
    write_id3_tags(metadata, mp3_path)
    print(f"Done, completed mp3 file available at: {mp3_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_link>")
        sys.exit(1)

    youtube_link = sys.argv[1]
    main(youtube_link)
