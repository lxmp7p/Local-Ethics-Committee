from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import request
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .functions.loadResearch import AddResearch, getResearchHistory, getMainResearchsList
from .models import *
# Create your views here.


class ResearchListView(View):
    """Переход к нужному типу исследования"""
    def loadResearch(request):
        return render(request, "research/researchType.html", {"method":"loadResearch"})

    def watchResearch(request):
        return render(request, "research/researchType.html", {"method":"watchResearch"})


class LoadResearch(View):
    """Загрузка исследования"""
    def get(self, request, researchType):
        researchList = None
        researchList = getMainResearchsList(researchType)
        return render(request, "research/loadResearch.html", {
            'researchType': researchType,
            'researchList': researchList,
        })

    def post(self, request, researchType):
        requestType = request.POST.get('typeRequest')
        relationshipStatus = request.POST.get('relationshipStatus')
        AddResearch(request=request, researchType=researchType, requestType=requestType, relationshipStatus=relationshipStatus)
        return render(request, "research/loadResearch.html", {
            'researchType': researchType,
            'requestType': requestType,
        })


class WatchResearch(View):
    """Просмотр списка исследований в системе"""
    def getResearchList(request, researchType):
        researchList = getMainResearchsList(researchType)
        return render(request, "research/researchList.html", {
            'researchList': researchList,
            'researchType': researchType,
        })

    def getResearch(request, researchId):
        if request.POST:
            Files.objects.get(id=request.POST.get("idFile")).delete()
        research, filesList, history = getResearchHistory(researchId)
        return render(request, "research/research.html", {
            'research': research,
            'filesList': filesList,
            'history': history,
        })

