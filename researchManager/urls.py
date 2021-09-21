from django.urls import path

from . import views
from . import ajax_views

urlpatterns = [
    path("", views.ResearchListView.loadResearch, name="researchTypeList"),
    path("loadResearch/<str:researchType>/", views.LoadResearch.as_view(), name="loadResearch"),
    path("ResearchTypeListViewForWatch/", views.ResearchListView.watchResearch, name="ResearchTypeListViewForWatch"),
    path("WatchResearchList/<str:researchType>/", views.WatchResearch.getResearchList, name="WatchResearchList"),
    path("WatchResearch/<int:researchId>/", views.WatchResearch.getResearch, name="watchResearch"),
    path("ajax/get_research_info/", ajax_views.get_research_info, name="get_research_info"),
  #  path("editResearch/deleteFile/<int:researchId>/<int:fileId>/", views.EditResearch.deleteFile, name="deleteFile"),
]