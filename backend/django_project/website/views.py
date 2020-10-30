from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from code_interaction.code_runners import *
from code_interaction.code_converters import *


def home(request):
    if request.method == 'GET':
        return HttpResponse("lol")


class ArticleView(APIView):
    def get(self, request):
        return Response({"articles": "articles"})


class TaskView(APIView):
    def get(self, request, task_name):
        return Response(["Print sum"])

    def post(self, request, task_name):
        return Response(request.body)
