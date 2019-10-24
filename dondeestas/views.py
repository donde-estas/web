import requests
from urllib.parse import parse_qsl
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import RegisterForm, GetKeyForm

BASE_URL = "http://donde-estas-api.herokuapp.com"


def get_landing_page(request):
    return HttpResponse(render(request, "index.html"))


def get_missing_list(request):
    return HttpResponse(render(request, "missing.html"))


def process_registration_view(request):
    if request.method != "POST":
        ctx = {"form": RegisterForm()}
        return HttpResponse(render(request, "register.html", context=ctx))
    if RegisterForm(request.POST).is_valid():
        query_params = request.body.decode()
        response = requests.post(f"{BASE_URL}/person?{query_params}")
        print(response, response.json())  # for debugging
        if response.ok and response.json()["success"]:
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def show_person(request, id):
    response = requests.get(f"{BASE_URL}/person/{id}")
    if response.status_code == 200:
        ctx = response.json()["payload"]
        return HttpResponse(render(request, "show-person.html", context=ctx))
    else:
        return HttpResponse(render(request, "index.html"))


