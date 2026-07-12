from yt_downloader import download_to_mp3

def main(youtube_link: str):
    mp3_path = download_to_mp3(youtube_link)
    print(f"Downloaded to {mp3_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_link>")
        sys.exit(1)

    youtube_link = sys.argv[1]
    main(youtube_link)
