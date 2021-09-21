from django.shortcuts import render
from django.views.generic import View
from researchManager.models import Research 
from django.contrib.auth import get_user_model

# Create your views here.


class CreateMeeting(View):
	"""Создание заседания"""
	def get(self, request):
		researchOnMeetinList = Research.objects.filter(date_accepted=None)
		User = get_user_model()
		userList = User.objects.all()
		return render(request, "createMeeting/createMeeting.html", {
			"researchOnMeetinList": researchOnMeetinList,
			"userList": userList,
		})
