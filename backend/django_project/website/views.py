import os
import sys
from pathlib import Path

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from code.code_runners import *
from code.code_converters import *


def home(request):
    if request.method == 'GET':
        return HttpResponse("lol")


class ArticleView(APIView):
    def get(self, request):
        return Response({"articles": "articles"})


def task(request, task_name):
    if request.method == "GET":
        return HttpResponse("print sum of numbers")

    if request.method == "POST":
        return HttpResponse(request.body)
