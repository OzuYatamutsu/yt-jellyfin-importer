from django.db import models

JOBSTATE_QUEUED = "QUEUED"
JOBSTATE_PROCESSING = "PROCESSING"
JOBSTATE_FAILED = "FAILED"
JOBSTATE_COMPLETED = "COMPLETED"


class Job(models.Model):
    youtube_url = models.URLField()
    status = models.CharField(max_length=100, default="QUEUED")
    log_line = models.CharField(max_length=1024, default="")
    percent = models.IntegerField(default=0)
    artist = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    finished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
