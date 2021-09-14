from django.shortcuts import render
from django.views.generic import View
from .functions.loadResearch import AddResearch
from .models import *
# Create your views here.

class ResearchTypeListView(View):
    """Выбор типа исследования для загрузки"""
    def get(self, request):
        return render(request, "research/researchType.html", {"method":"loadResearch"})


class ResearchRequestTypeListView(View):
    """Выбор типа заявки для загрузки"""
    def get(self, request, researchType):
        return render(request, "research/researchRequestType.html", {'researchType': researchType})


class LoadResearch(View):
    """Загрузка исследования"""
    def get(self, request, researchType, requestType):
        researchList = None
        if requestType == 'secondRelationRequest':
            researchList = Researh.objects.filter(type=researchType)
        print(researchList)
        return render(request, "research/loadResearch.html", {
            'researchType': researchType,
            'requestType': requestType,
            'researchList': researchList,
        })

    def post(self, request, researchType, requestType):
        AddResearch(request=request, researchType=researchType, requestType=requestType)
        return render(request, "research/loadResearch.html", {
            'researchType': researchType,
            'requestType': requestType,
        })


class ResearchTypeListViewForWatch(View):
    """Выбор типа исследования для загрузки"""
    def get(self, request):
        return render(request, "research/researchType.html", {"method":"watchResearch"})


class WatchResearchList(View):
    """Просмотр списка исследований в системе"""
    def get(self, request, researchType):
        researchList = Researh.objects.filter()
        return render(request, "research/researchList.html", {
            'researchList': researchList,
            'researchType': researchType,
        })


class WatchResearch(View):
    """Просмотри исследования"""
    def get(self, request, researchId):
        research = Researh.objects.get(id=researchId)
        filesList = Files.objects.filter(research=research)
        return render(request, "research/research.html", {
            'research': research,
            'filesList': filesList,
        })


