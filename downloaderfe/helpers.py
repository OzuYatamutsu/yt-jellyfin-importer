from downloaderfe.models import Job


def log(job: Job, percent: int, text: str) -> None:
    print(text)

    job.percent = percent
    job.log_line = text
    job.save()
