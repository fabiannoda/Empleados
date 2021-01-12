from django.contrib import admin
from django.urls import path


def Desde(self):
    print("puto el que lo lea -----------------------------------------")


urlpatterns = [
    path('departamento/', Desde),
]
