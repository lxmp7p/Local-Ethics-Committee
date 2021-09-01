from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .models import Researh
# Create your views here.

class ResearhTypeListView(View):
    """Выбор типа исследования для загрузки"""
    def get(self, request):
        return render(request, "research/researchType.html")


class ResearhRequestTypeListView(View):
    """Выбор типа заявки для загрузки"""
    def get(self, request, researhType):
        return render(request, "research/researchRequestType.html", {'researhType': researhType})

class LoadResearch(View):
    """Загрузка исследования"""
    def get(self, request, researhType, requestType):
        if researhType == "clinicalResearch":
            return render(request, "research/loadResearch.html")
        return render(request, "research/loadResearch.html")