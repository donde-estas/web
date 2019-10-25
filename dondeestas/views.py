import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, resolve_url
from django.conf import settings
from .forms import RegisterForm, FindPersonForm


CARDS_PER_LINE = 3


def get_landing_page(request):
    return HttpResponse(render(request, "index.html"))

def get_people(request):
    people = requests.get(f"{settings.BASE_API_URL}/missing").json()
    payload = people["payload"] if people["success"] else []
    padding = [None] * (len(payload) % CARDS_PER_LINE)
    ctx = {"people": payload + padding, "cards_per_line": CARDS_PER_LINE}
    return HttpResponse(render(request, "people.html", ctx))

def process_registration_view(request):
    if request.method != "POST":
        ctx = {"form": RegisterForm()}
        return HttpResponse(render(request, "register.html", ctx))
    if RegisterForm(request.POST).is_valid():
        payload = request.POST.dict()
        del payload['csrfmiddlewaretoken']
        payload['latitude'] = -33.436961
        payload['longitude'] = -70.634372
        payload['last_seen'] = True
        response = requests.post(f"{settings.BASE_API_URL}/person", params=payload)
        print(response, response.json())  # for debugging
        if response.ok and response.json()["success"]:
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def show_person(request, pid):
    response = requests.get(f"{settings.BASE_API_URL}/person/{pid}")
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
        response = requests.patch(f"{settings.BASE_API_URL}/missing/{pid}", params={'plain_key': request.POST['key']})
        if response.ok and response.json()["success"]:
            return JsonResponse({"success": True,
                                 "url": resolve_url('person.show', pid=pid)})
    return JsonResponse({"success": False,
                         "url": resolve_url('person.findform', pid=pid)})

def find_person_with_key(request, pid, key):
    ctx = {
        "form": FindPersonForm(),
        "pid": pid,
        "key": key,
        }
    return HttpResponse(render(request, "find-person-auto.html", context=ctx))
