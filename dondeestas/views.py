import requests
from urllib.parse import parse_qsl
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import RegisterForm

BASE_URL = "http://donde-estas.herokuapp.com"
CARDS_PER_LINE = 3


def get_landing_page(request):
    return HttpResponse(render(request, "index.html"))


def get_people(request):
    print("HEHE")
    people = requests.get(f"{BASE_URL}/missing").json()
    payload = people["payload"] if people["success"] else []
    padding = [None] * (len(payload) % CARDS_PER_LINE)
    ctx = {
        "people": payload + padding,
        "cards_per_line": CARDS_PER_LINE,
    }
    return HttpResponse(render(request, "people.html", ctx))


def process_registration_view(request):
    if request.method != "POST":
        ctx = {"form": RegisterForm()}
        return HttpResponse(render(request, "register.html", ctx))
    if RegisterForm(request.POST).is_valid():
        query_params = request.body.decode()
        response = requests.post(f"{BASE_URL}/person?{query_params}")
        print(response, response.json())  # for debugging
        if response.ok and response.json()["success"]:
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})
