from yt_downloader import download_to_mp3
from acoustid_interface import resolve_audio_fp
from musicbrainz_interface import resolve_release, download_cover_art
from config import DOWNLOAD_LOCATION
from id3_interface import write_id3_tags
from os.path import basename
from os import rename, getcwd


def main(youtube_link: str):
    print("[1/5] Downloading and converting to mp3...")
    mp3_path = download_to_mp3(youtube_link)
    print(f"Downloaded to {mp3_path}")
    print("[2/5] Generating audio fingerprint and resolving initial metadata...")
    metadata = resolve_audio_fp(mp3_path)
    print(f"Audio fingerprint and metadata resolved: {metadata}")
    if not metadata:
        print("No metadata found!! Aborting!!")
        exit(1)
    print("[3/5] Resolving release...")
    metadata = resolve_release(metadata.recording_id, metadata)
    print(f"Release information resolved.")
    print("[4/5] Downloading cover art...")
    metadata.album_art = download_cover_art(metadata.release_id)
    print(f"Cover art downloaded: {len(metadata.album_art)} bytes")
    print("[5/5] Writing ID3 tags...")
    write_id3_tags(metadata, mp3_path)
    output_path = mp3_path.replace(basename(mp3_path), f"{metadata.artist} - {metadata.title}.mp3")
    output_path = output_path.replace(DOWNLOAD_LOCATION, getcwd())
    rename(mp3_path, output_path)
    print(f"Done, completed mp3 file available at: {output_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_link>")
        sys.exit(1)

    youtube_link = sys.argv[1]
    main(youtube_link)
