from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .functions.loadResearch import AddResearch
from .models import *
# Create your views here.


class ResearchListView(View):
    """Переход к нужному типу исследования"""
    def loadResearch(request):
        return render(request, "research/researchType.html", {"method":"loadResearch"})

    def watchResearch(request):
        return render(request, "research/researchType.html", {"method":"watchResearch"})

    def getResearchRequestTypeList(request, researchType):
        return render(request, "research/researchRequestType.html", {'researchType': researchType})


class LoadResearch(View):
    """Загрузка исследования"""
    def get(self, request, researchType, requestType):
        researchList = None
        if requestType == 'secondRelationRequest':
            researchList = Research.objects.filter(type=researchType)
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


class WatchResearch(View):
    """Просмотр списка исследований в системе"""
    def getResearchList(request, researchType):
        researchList = Research.objects.filter()
        return render(request, "research/researchList.html", {
            'researchList': researchList,
            'researchType': researchType,
        })

    def getResearch(request, researchId):
        research = Research.objects.get(id=researchId)
        filesList = Files.objects.filter(research=research)
        history = []
        for historyResearch in Research.objects.filter(identityCode=research.identityCode):
            historyFiles = Files.objects.filter(research=research)
            history.append({"historyResearch": historyResearch, "historyFiles": historyFiles})
        return render(request, "research/research.html", {
            'research': research,
            'filesList': filesList,
            'history': history,
        })