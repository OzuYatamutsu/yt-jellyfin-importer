from django.db import models


class Job(models.Model):
    youtube_url = models.URLField()
    status = models.CharField(max_length=100, default="Queued")
    percent = models.IntegerField(default=0)
    artist = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    output_file = models.FileField(upload_to="downloads/", blank=True)
    finished = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
