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
                    get_missing_list,
                    process_registration_view,
                    show_person)

urlpatterns = [
    path("", get_landing_page, name="landing"),
    path("missing", get_missing_list, name="missing"),
    path("register", process_registration_view, name="register"),
    path("person/<int:id>", show_person, name="person.show"),
]
