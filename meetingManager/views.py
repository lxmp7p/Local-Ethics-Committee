from django.shortcuts import render
from django.views.generic import View
from researchManager.models import Research 
from django.contrib.auth import get_user_model
from .models import MeetingData
from .models import Meeting as MeetingModel
from .functions.createMeeting import createMeeting
from .functions.report_maker import createReport

# Create your views here.

class Meeting(View):
	def getNotAcceptedResearch():
		return Research.objects.filter(addedOnMeeting=False, date_accepted=None)

	def getUserList():
		User = get_user_model()
		return User.objects.all()

	def getMeetingList():
		return MeetingModel.objects.all()


class CreateMeeting(Meeting):
	"""Создание заседания"""
	def get(self, request):
		return render(request, "createMeeting/createMeeting.html", {
			"researchOnMeetinList": Meeting.getNotAcceptedResearch(),
			"userList": Meeting.getUserList(),
		})

	def post(self, request):
		meeting, researchListInMeeting, randNumber = createMeeting(request)	#rund number need to save valid name subpoena
		getReportInfoList = createReport(researchListInMeeting, meeting, randNumber)
		return render(request, "createMeeting/createMeeting.html", {
			"researchOnMeetinList": Meeting.getNotAcceptedResearch(),
			"userList": Meeting.getUserList(),
		})


class MeetingList(Meeting):
	def get(self, request):
		meetingList = Meeting.getMeetingList()
		return render(request, "meetingList.html", {
			"meetingList": meetingList,
		})

