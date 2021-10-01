from django.contrib.contenttypes.models import ContentType
from ..models import Meeting, MeetingData
from researchManager.models import Research
import datetime
import time as getTime
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE # these are action flags from the docs

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
		objResearch.date_accepted = request.POST.get("date")
		objResearch.save()
		researchList.append(objResearch)

	for user in request.POST.getlist("userIdList"):
		MeetingData.objects.create(
			usersInMeeting_id=user,
			meeting=meeting,
	) 
	# '| ' + informationForm.type_request + ' | ' + get_typeResearch(researchType) + ' : ' + folderName
	meetingId = Meeting.objects.all().last()
	LogEntry.objects.log_action(
    	user_id = request.user.id,
        content_type_id = ContentType.objects.get_for_model(Meeting).pk,
        object_repr = request.POST.get("date"), 
        object_id = meetingId.id,
        change_message = '| '  + 'Создано заседание' + ' | ', 
        action_flag = ADDITION)



	return meeting, researchList, randNumber


#def getNormalDate(invalidDate):
	#invalidDate = 2021-09-27