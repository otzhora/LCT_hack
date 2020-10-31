import os
from pathlib import Path
import json

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from code_interaction.code_runners import *
from code_interaction.code_converters import *

ASSIGNMENTS_PATH = Path(os.getcwd())/"assignments"/"tasks"
STUDENT_SOLUTIONS_PATH = Path(os.getcwd())/"assignments"/"students"


def home(request):
    if request.method == 'GET':
        return HttpResponse("lol")


class ArticleView(APIView):
    def get(self, request):
        return Response({"articles": "articles"})


class TaskView(APIView):
    def get(self, request, url):
        task = Task.objects.get(url=url)
        serializer = TaskSerializer(task)
        return Response({"task": serializer.data})

    def post(self, request, url):
        body = json.loads(request.body)
        task = Task.objects.get(url=url)

        username = body["username"]
        text = body["text"]
        lang = body["lang"]

        converter = CodeConverter(STUDENT_SOLUTIONS_PATH)
        converter.text_to_code(username, url, text, lang)

        task_path = task.path
        solution_path = converter.get_code_path(username, url)

        runner = Languages[lang](solution_path, task_path, hooks={"style"})
        res = runner.run_code()
        return Response(res)


