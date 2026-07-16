from downloaderfe.models import Job
from threading import Thread


def create_job(youtube_link: str) -> int:
    job = Job.objects.create()
    Thread(
        target=handle_download_to_jellyfin_dir,
        args=(job, youtube_link),
        daemon=True
    )
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
    pass  # TODO
