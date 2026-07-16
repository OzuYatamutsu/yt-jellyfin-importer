from downloaderfe.downloader_interface import create_job, get_status
from django.shortcuts import render
from django.http import JsonResponse
from django import Request
from json import loads


def index(request: Request):
    return render(request, "downloaderfe/index.html")


def start_job(request: Request) -> JsonResponse:
    youtube_link = loads(request.body)["link"]

    return JsonResponse({
        "id": create_job(youtube_link)
    })


def status(_request: Request, job_id: int) -> JsonResponse:
    return JsonResponse(get_status(job_id))
