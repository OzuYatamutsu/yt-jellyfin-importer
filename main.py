from yt_downloader import download_to_mp3
from acoustid_interface import resolve_audio_fp

def main(youtube_link: str):
    print("[1/3] Downloading and converting to mp3...")
    mp3_path = download_to_mp3(youtube_link)
    print(f"Downloaded to {mp3_path}")
    print("[2/3] Generating audio fingerprint and resolving initial metadata...")
    metadata = resolve_audio_fp(mp3_path)
    print(f"Audio fingerprint and metadata resolved: {metadata}")
    print("[3/3] Resolving release id...")
    

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_link>")
        sys.exit(1)

    youtube_link = sys.argv[1]
    main(youtube_link)
