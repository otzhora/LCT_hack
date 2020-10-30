from django.shortcuts import render
from django.http import HttpResponse

# from code.code_runners import *
# from code.code_converters import *


def home(request):
    if request.method == 'GET':
        return HttpResponse("lol")


def task(request):
    pass