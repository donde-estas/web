"""dondeestas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (get_landing_page,
                    get_people,
                    process_registration_view,
                    show_person,
                    find_form_person,
                    find_person,
                    find_person_with_key)

urlpatterns = [
    path("", get_landing_page, name="landing"),
    path("people", get_people, name="people"),
    path("register", process_registration_view, name="register"),
    path("person/<int:pid>", show_person, name="person.show"),
    path("person/<int:pid>/getkey", find_form_person, name="person.findform"),
    path("person/<int:pid>/find", find_person, name="person.find"),
    path("person/<int:pid>/find/<str:key>", find_person_with_key, name="person.find.with.key"),
]
