from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateMeeting.as_view(), name="createMeeting"),
    path("meetingList", views.MeetingList.as_view(), name="meetingList"),
]