import os
from pathlib import Path
import json

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
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
    def get(self, request, task_name):
        task = Task.objects.get(url=task_name)
        return Response(task.task)

    def post(self, request, task_name):
        body = json.loads(request.body)
        task = Task.objects.get(url=task_name)

        username = body["username"]
        text = body["text"]
        lang = body["lang"]

        converter = CodeConverter(STUDENT_SOLUTIONS_PATH)
        converter.text_to_code(username, task_name, text, lang)

        task_path = task.path
        solution_path = converter.get_code_path(username, task_name)

        runner = Languages[lang](solution_path, task_path, hooks={"style"})
        res = runner.run_code()
        return Response(res)
