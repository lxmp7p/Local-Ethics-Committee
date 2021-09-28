from ..models import Meeting, MeetingData
from researchManager.models import Research
import datetime
import time as getTime

now = datetime.datetime.now()


def createMeeting(request):
	randNumber = str(round(getTime.time() * 1000))
	meeting = Meeting.objects.create(
		date=request.POST.get("date"),
		time=request.POST.get("time"),
		subpoena = f'reports/{str(now.strftime("%d-%m-%Y-%H"))}/subpoena{randNumber}.docx',
	)
	researchList = []
	for research in request.POST.getlist("researchIdList"):
		MeetingData.objects.create(
			researchsInMeeting_id=research,
			meeting=meeting,
		)
		objResearch = Research.objects.get(id=research)
		objResearch.addedOnMeeting = True
		objResearch.save()
		researchList.append(objResearch)

	for user in request.POST.getlist("userIdList"):
		MeetingData.objects.create(
			usersInMeeting_id=user,
			meeting=meeting,
	)
	return meeting, researchList, randNumber


#def getNormalDate(invalidDate):
	#invalidDate = 2021-09-27