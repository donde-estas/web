from django.http import HttpResponse
from django.shortcuts import render


def get_landing_page(request):
    return HttpResponse(render(request, "index.html"))


def get_missing_list(request):
    return HttpResponse(render(request, "missing.html"))


def get_register_form(request):
    return HttpResponse(render(request, "register.html"))
