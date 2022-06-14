import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from bankrupt import settings
from .models import Calls


def index(request):
    return render(request, 'bankrupt_app/index.html')

@csrf_exempt
def call_me(request):
    if request.method == "POST":
        i_data = json.loads(request.body)
        print(i_data["phone"], i_data["name"])

        try:
            Calls(name=i_data["name"], phone=i_data["phone"]).save()
            data = {"status": "success"}
        except Exception as e:
            print(e)
            data = {"status": "error"}

        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def quiz(request):
    if request.method == "POST":
        print("Quiz: ", request.POST)
        data = {
            "quiz": True
        }
        data = json.dumps(data)
        return HttpResponse(data, content_type="application/json")