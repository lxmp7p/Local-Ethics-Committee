from django.urls import path

from . import views

urlpatterns = [
    path("", views.ResearchTypeListView.as_view(), name="researchTypeList"),
    path("researhRequestType/<str:researchType>/", views.ResearchRequestTypeListView.as_view(), name="researchRequestTypeList"),
    path("loadResearch/<str:researchType>/<str:requestType>", views.LoadResearch.as_view(), name="loadResearch"),
]