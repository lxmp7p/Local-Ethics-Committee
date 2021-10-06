from django.urls import path

from . import views
from . import ajax_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
    path("", login_required(TemplateView.as_view(template_name="research/researchType.html")), name="researchTypeList"),
    path("loadResearch/<str:researchType>/", login_required(views.LoadResearch.as_view()), name="loadResearch"),
    path("WatchResearchList/<str:researchType>/", login_required(views.WatchResearch.getResearchList), name="WatchResearchList"),
    path("WatchResearch/<int:researchId>/", login_required(views.WatchResearch.getResearch), name="watchResearch"),
    path("ajax/get_research_info/", login_required(ajax_views.get_research_info), name="get_research_info"),
  #  path("editResearch/deleteFile/<int:researchId>/<int:fileId>/", views.EditResearch.deleteFile, name="deleteFile"),
]