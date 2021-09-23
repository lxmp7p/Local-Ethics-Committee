from ..models import Meeting, MeetingData
from researchManager.models import Research
import datetime

now = datetime.datetime.now()


def createMeeting(request):
	meeting = Meeting.objects.create(
		date=request.POST.get("date"),
		time=request.POST.get("time"),
		subpoena = f'reports/{str(now.strftime("%d-%m-%Y-%H-%M-%S"))}/subpoena.docx',
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
	return meeting, researchList
