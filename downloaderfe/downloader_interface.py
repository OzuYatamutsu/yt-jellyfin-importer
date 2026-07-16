from downloaderfe.models import (
    Job, JOBSTATE_COMPLETED, JOBSTATE_FAILED, JOBSTATE_PROCESSING
)
from downloaderbe.musicbrainz_interface import (
    resolve_release, download_cover_art
)
from downloaderbe.jellyfin_interface import move_file_to_jellyfin_dir
from downloaderbe.acoustid_interface import resolve_audio_fp
from downloaderbe.yt_downloader import download_to_mp3
from downloaderbe.id3_interface import write_id3_tags
from downloaderfe.helpers import log
from threading import Thread
from os.path import basename
from shutil import move
import downloaderbe.config as config


def create_job(youtube_link: str) -> int:
    job = Job.objects.create()
    job.youtube_url = youtube_link
    job.save()

    Thread(
        target=handle_download_to_jellyfin_dir,
        args=(job, youtube_link),
        daemon=True
    ).start()
    return job.id


def get_status(job_id: int) -> dict:
    job = Job.objects.get(pk=job_id)

    return {
        "status": job.status,
        "percent": job.percent,
        "log_line": job.log_line,
        "finished": job.finished
    }


def handle_download_to_jellyfin_dir(job: Job, youtube_link: str) -> None:
    try:
        job.status = JOBSTATE_PROCESSING
        job.save()

        log(job, 0, "[1/5] Downloading and converting to mp3...")
        mp3_path = download_to_mp3(youtube_link)
        log(job, 20, f"Downloaded to {mp3_path}")

        log(job, 20, "[2/5] Generating audio fingerprint and resolving initial metadata...")
        metadata = resolve_audio_fp(mp3_path)
        job.artist = metadata.artist
        job.title = metadata.title
        job.save()
        log(job, 40, f"Audio fingerprint and metadata resolved: {metadata}")

        if not metadata:
            log(job, 100, "No metadata found!! Aborting!!")
            job.status = JOBSTATE_FAILED
            job.finished = True
            return

        log(job, 40, f"[3/5] Resolving release...")
        metadata = resolve_release(metadata.recording_id, metadata)
        log(job, 60, f"Release information resolved.")

        log(job, 60, "[4/5] Downloading cover art...")
        metadata.album_art = download_cover_art(metadata.release_id)
        log(job, 80, f"Cover art downloaded: {len(metadata.album_art)} bytes")

        log(job, 80, "[5/5] Writing ID3 tags...")
        write_id3_tags(metadata, mp3_path)
        output_path = mp3_path.replace(basename(mp3_path), f"{metadata.artist} - {metadata.title}.mp3")
        output_path = output_path.replace(config.DOWNLOAD_LOCATION, config.OUTPUT_LOCATION)
        move(mp3_path, output_path)
        log(job, 100, f"Done, completed mp3 file available at: {output_path}")

        log(job, 100, "Moving to jellyfin...")
        output_path = move_file_to_jellyfin_dir(metadata)
        job.status = JOBSTATE_COMPLETED
        job.finished = True
        job.save()
        log(job, 100, f"Done, moved mp3 file to {output_path}.")
    except Exception as e:
        log(job, 100, f"Job failed due to error: {e}")
        job.status = JOBSTATE_FAILED
        job.finished = True
        job.save()
