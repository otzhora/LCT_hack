import os
from pathlib import Path
import json
import subprocess

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
    def get(self, request, url):
        task = Task.objects.get(url=url)
        return Response(task.task)

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


class CodeView(APIView):
    def get(self, request, username, url):
        converter = CodeConverter(STUDENT_SOLUTIONS_PATH)
        solution_path = converter.get_code_path(username, url)

        solutions = [f"{solution_path}/{solution}" for solution in os.listdir(solution_path)]
        resp = []
        for solution in solutions:
            with open(solution, "r") as f:
                resp.append("".join(f.readlines()))
        return Response(resp)


class NewTaskView(APIView):
    def post(self, request):
        zip_test = request.FILES["data"]
        body = dict(request.POST)
        url = body["url"][0]
        title = body["title"][0]
        desc = body["description"][0]

        zip_path = f"{ASSIGNMENTS_PATH}/{url}.zip"
        with open(zip_path, "wb+") as f:
            for chunk in zip_test.chunks():
                f.write(chunk)

        task_path = f"{ASSIGNMENTS_PATH}/{url}"
        if os.path.isdir(task_path):
            subprocess.run(["rm", "-rf", task_path])

        subprocess.run(["unzip", zip_path, "-d", f"{ASSIGNMENTS_PATH}"])
        subprocess.run(["rm", zip_path])

        # TODO: add a new task to db

        return Response("Biba")
