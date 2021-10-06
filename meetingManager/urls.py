from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", login_required(views.CreateMeeting.as_view()), name="createMeeting"),
    path("meetingList", login_required(views.MeetingList.as_view()), name="meetingList"),
]