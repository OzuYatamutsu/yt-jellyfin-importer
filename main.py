from musicbrainz_interface import resolve_release, download_cover_art
from jellyfin_interface import move_file_to_jellyfin_dir
from acoustid_interface import resolve_audio_fp
from yt_downloader import download_to_mp3
from id3_interface import write_id3_tags
from argparse import ArgumentParser
from typing import Optional
from os.path import basename
from shutil import move
import config


def main(youtube_link: str, jellyfin_lib_location: Optional[str]):
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
    output_path = output_path.replace(config.DOWNLOAD_LOCATION, config.OUTPUT_LOCATION)
    move(mp3_path, output_path)
    print(f"Done, completed mp3 file available at: {output_path}")
    
    if jellyfin_lib_location:
        print("Moving to jellyfin...")
        output_path = move_file_to_jellyfin_dir(metadata)
        print(f"Done, moved mp3 file to {output_path}.")


def _set_config_from_args() -> None:
    arg_parser = ArgumentParser()
    arg_parser.add_argument("youtube_link")
    arg_parser.add_argument(
        "--jellyfin-library",
        help=(
            "If set, moves processed music to the proper directory "
            "under this library root directory. For example, a value "
            "of /lib/music and processed file of album=My Album, "
            "artist=My Artist, song=My Song will be output to "
            "/var/lib/My Artist/My Album/My Artist - My Song.mp3."
        )
    )
    arg_parser.add_argument(
        "--download-location",
        help=(
            "Where should we download intermediate files for processing? "
            "(default: new temporary directory.)"
        )
    )
    arg_parser.add_argument(
        "--acoustid-api-key",
        help=(
            "API key to access the Acoustid API (required). By default, this is read from "
            "ACOUSTID_API_KEY env variable, but can also be specified here. "
            "If not specified, reads the API key from config.py."
        )
    )

    args = arg_parser.parse_args()
    config.YOUTUBE_LINK = args.youtube_link
    if (args.jellyfin_library):
        config.JELLYFIN_LIBRARY = args.jellyfin_library
    if (args.download_location):
        config.DOWNLOAD_LOCATION = args.download_location
    if (args.acoustid_api_key):
        config.ACOUSTID_API_KEY = args.acoustid_api_key


if __name__ == "__main__":
    _set_config_from_args()
    main(config.YOUTUBE_LINK, config.JELLYFIN_LIBRARY)
