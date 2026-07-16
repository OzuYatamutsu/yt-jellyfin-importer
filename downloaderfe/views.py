from downloaderfe.downloader_interface import create_job, get_status
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.shortcuts import render
from json import loads


def index(request: HttpRequest):
    return render(request, "downloaderfe/index.html")


def start_job(request: HttpRequest) -> JsonResponse:
    youtube_link = loads(request.body)["link"]

    return JsonResponse({
        "id": create_job(youtube_link)
    })


def status(_request: HttpRequest, job_id: int) -> JsonResponse:
    return JsonResponse(get_status(job_id))
