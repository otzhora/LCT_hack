import os
from pathlib import Path
import json
import subprocess
from collections import defaultdict

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers

from .models import Task, Teacher, Student, TaskResult, CodeReview
from .serializers import TaskSerializer
from code_interaction.code_runners import *
from code_interaction.code_converters import *
from code_interaction.advanced_code_runner import *


ASSIGNMENTS_PATH = Path(os.getcwd()) / "assignments" / "tasks"
STUDENT_SOLUTIONS_PATH = Path(os.getcwd()) / "assignments" / "students"
ADVANCED_PATH = Path(os.getcwd()) / "assignments" / "advanced_tasks"


def home(request):
    if request.method == 'GET':
        return HttpResponse("lol")


class ArticleView(APIView):
    def get(self, request):
        return Response({"articles": "articles"})


class TasksView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})


class TaskView(APIView):
    def get(self, request, url):
        task = Task.objects.get(url=url)
        serializer = TaskSerializer(task)
        return Response({"task": serializer.data})

    def post(self, request, url):
        print(request.body)
        body = json.loads(request.body)

        task = Task.objects.get(url=url)

        username = body["username"]
        text = body["text"]
        lang = body["lang"]

        converter = CodeConverter(STUDENT_SOLUTIONS_PATH)
        converter.text_to_code(username, url, text, lang)

        task_path = task.path
        print(task_path)
        solution_path = converter.get_code_path(username, url)

        print(solution_path)
        runner = Languages[lang](solution_path, task_path, hooks={"style"})
        res = runner.run_code()

        student, created1 = Student.objects.get_or_create(
            name=username,
        )
        true_count = 0
        for i in res:
            if i["check"]:
                true_count += 1
        _ = TaskResult.objects.create(
            task=task,
            student=student,
            mark=true_count / len(res),
        )
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
        if Task.objects.filter(url=url).exists():
            return Response(f"Task with name {url} already exists")
        title = body["title"][0]
        teacher = body["teacher"][0]
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

        task = Task()
        task.title = title
        task.task = desc
        task.path = task_path
        task.url = url
        #task.teacher = Teacher.objects.get(name=teacher)
        task.save()

        return Response("Biba")


class ResultView(APIView):
    def get(self, request, username, url):
        student_obj = Student.objects.get(name=username)
        task_obj = Task.objects.get(url=url)
        res = list(TaskResult.objects.filter(student=student_obj, task=task_obj))
        return Response([i.mark for i in res])

users2assignments = defaultdict(list)


class AssignView(APIView):
    def get(self, request, username):
         return Response(users2assignments[username])

    def post(self, request):
        print(request.body)
        body = json.loads(request.body)
        username = body["username"]
        url = body["url"]
        users2assignments[username].append(url)
        return Response(users2assignments[username])


users2review = defaultdict(dict)


class ReviewView(APIView):
    def get(self, request, username, url):
        if url in users2review[username]:
            return Response(users2review[username][url])

    def post(self, request):
        body = json.loads(request.body)
        username = body["username"]
        task_url = body["url"]
        comment = body["comment"]

        users2review[username][task_url] = comment
        return Response(users2review[username][task_url])


class AdvancedView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        git_url = body["git_url"]

        run_script = ADVANCED_PATH / "run.sh"
        checks_script = ADVANCED_PATH / "pre_run.sh"
        setup_script = ADVANCED_PATH / "setup.sh"
        runner = CodeManager(git_url, CodeRunner, setup_script, checks_script, run_script)
        return Response(runner.run_code())
