from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


class LandingPageView(View):
    def get(self, request):
        return HttpResponse(render(request, "index.html"))
