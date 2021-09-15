from django.urls import path

from . import views

urlpatterns = [
    path("", views.ResearchListView.loadResearch, name="researchTypeList"),
    path("researhRequestType/<str:researchType>/", views.ResearchListView.getResearchRequestTypeList, name="researchRequestTypeList"),
    path("loadResearch/<str:researchType>/<str:requestType>", views.LoadResearch.as_view(), name="loadResearch"),
    path("ResearchTypeListViewForWatch/", views.ResearchListView.watchResearch, name="ResearchTypeListViewForWatch"),
    path("WatchResearchList/<str:researchType>/", views.WatchResearch.getResearchList, name="WatchResearchList"),
    path("WatchResearch/<int:researchId>/", views.WatchResearch.getResearch, name="watchResearch"),
]