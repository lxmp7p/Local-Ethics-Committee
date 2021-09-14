from django.urls import path

from . import views

urlpatterns = [
    path("", views.ResearchTypeListView.as_view(), name="researchTypeList"),
    path("researhRequestType/<str:researchType>/", views.ResearchRequestTypeListView.as_view(), name="researchRequestTypeList"),
    path("loadResearch/<str:researchType>/<str:requestType>", views.LoadResearch.as_view(), name="loadResearch"),
    path("ResearchTypeListViewForWatch/", views.ResearchTypeListViewForWatch.as_view(), name="ResearchTypeListViewForWatch"),
    path("WatchResearchList/<str:researchType>/", views.WatchResearchList.as_view(), name="WatchResearchList"),
    path("WatchResearch/<int:researchId>/", views.WatchResearch.as_view(), name="watchResearch"),
]