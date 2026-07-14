from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, "downloaderfe/index.html")


def start_job(request):
    return JsonResponse({
        "id": 123
    })


def status(request, job_id):
    return JsonResponse({
        "percent": 50,
        "message": "Downloading...",
        "finished": False,
    })

