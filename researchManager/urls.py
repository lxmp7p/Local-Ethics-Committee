from django.urls import path

from . import views

urlpatterns = [
    path("", views.ResearhTypeListView.as_view(), name="researhTypeList"),
    path("researhRequestType/<str:researhType>/", views.ResearhRequestTypeListView.as_view(), name="researhRequestTypeList"),
    path("loadResearch/<str:researhType>/<str:requestType>", views.LoadResearch.as_view(), name="loadResearch"),
]