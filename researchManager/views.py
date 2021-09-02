from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .models import Researh
# Create your views here.

class ResearchTypeListView(View):
    """Выбор типа исследования для загрузки"""
    def get(self, request):
        return render(request, "research/researchType.html")


class ResearchRequestTypeListView(View):
    """Выбор типа заявки для загрузки"""
    def get(self, request, researchType):
        return render(request, "research/researchRequestType.html", {'researchType': researchType})


class LoadResearch(View):
    """Загрузка исследования"""
    def get(self, request, researchType, requestType):
        return render(request, "research/loadResearch.html", {
            'researchType': researchType,
            'requestType': requestType,
        })

    def post(self, request, researchType, requestType):
        print(request.POST)
        return render(request, "research/loadResearch.html", {
            'researchType': researchType,
            'requestType': requestType,
        })
