import requests
from urllib.parse import parse_qsl
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, resolve_url
from json import dumps
from .forms import RegisterForm, FindPersonForm

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
        payload = request.POST.dict()
        del payload['csrfmiddlewaretoken']
        payload['latitude'] = -33.436961
        payload['longitude'] = -70.634372
        payload['last_seen'] = True
        response = requests.post(f"{BASE_URL}/person", params=payload)
        print(response, response.json())  # for debugging
        if response.ok and response.json()["success"]:
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def show_person(request, pid):
    response = requests.get(f"{BASE_URL}/person/{pid}")
    if response.status_code == 200:
        ctx = response.json()["payload"]
        return HttpResponse(render(request, "show-person.html", context=ctx))
    else:
        return redirect('landing')

def find_form_person(request, pid):
    ctx = {
        "form": FindPersonForm(),
        "pid": pid,
        }
    return HttpResponse(render(request, "find-person.html", context=ctx))

def find_person(request, pid):
    if request.method != "POST":
        return redirect('landing')
    if FindPersonForm(request.POST).is_valid():
        print(pid, request.POST['key'])
        response = requests.patch(f"{BASE_URL}/missing/{pid}", params={'plain_key': request.POST['key']})
        if response.ok and response.json()["success"]:
            return JsonResponse({"success": True,
                                 "url": resolve_url('person.show', pid=pid)})
    return JsonResponse({"success": False,
                         "url": resolve_url('person.findform', pid=pid)})

def find_person_with_key(request, pid, key):
    # if request.method != "POST":
    #     return redirect('landing')
    # if FindPersonForm(request.POST).is_valid():
    #     print(pid, request.POST['key'])
    #     response = requests.patch(f"{BASE_URL}/missing/{pid}", params={'plain_key': request.POST['key']})
    #     if response.ok and response.json()["success"]:
    #         return JsonResponse({"success": True, "url": resolve_url('person.show', pid=pid)})
    # return JsonResponse({"success": False})
    ctx = {
        "form": FindPersonForm(),
        "pid": pid,
        "key": key,
        }
    return HttpResponse(render(request, "find-person-auto.html", context=ctx))
