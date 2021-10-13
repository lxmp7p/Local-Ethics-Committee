from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.files.base import File
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from .functions.loadResearch import AddResearch, getResearchHistory, getMainResearchsList
from .models import *
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION # these are action flags from the docs


class LoadResearch(View):
    """Загрузка исследования"""
    def get(self, request, researchType):
        researchList = getMainResearchsList(researchType)
        return render(request, "research/loadResearch.html", {
            'researchType': researchType,
            'researchList': researchList,
        })

    def post(self, request, researchType):
        requestType = request.POST.get('typeRequest')
        relationshipStatus = request.POST.get('relationshipStatus')
        AddResearch(request=request, researchType=researchType, requestType=requestType, relationshipStatus=relationshipStatus)
        return render(request, "research/researchType.html")


class WatchResearch(View):
    """Просмотр списка исследований в системе"""
    def getResearchList(request, researchType):
        researchList = getMainResearchsList(researchType)
        print(Research.objects.all())
        return render(request, "research/researchList.html", {
            'researchList': researchList,
            'researchType': researchType,
        })

    def getResearch(request, researchId):
        if request.POST:
            File = Files.objects.get(id=request.POST.get("idFile"))
           
            LogEntry.objects.log_action(
            user_id=request.user.id,
            content_type_id=ContentType.objects.get_for_model(Files).pk,
            object_repr=File.name, 
            object_id=File.id,
            change_message='| ' + File.name + ' Версия: ' + File.version + ' | ' + str(File.research.type) + ' | ' + str(File.research.getSubName())  + ' | ', 
            action_flag=DELETION,
            )
            Files.objects.get(id=request.POST.get("idFile")).delete()


        research, filesList, history = getResearchHistory(researchId)
        return render(request, "research/research.html", {
            'research': research,
            'filesList': filesList,
            'history': history,
        })
