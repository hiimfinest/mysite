from django.shortcuts import render

# Create your views here.

from django.urls import path

from django.http import HttpResponse


def index(request):
    return HttpResponse('gucci gang')