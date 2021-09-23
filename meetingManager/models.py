from django.db import models
from django.conf import settings
from researchManager.models import Research
# Create your models here.


class Meeting(models.Model):
	"""Исследования"""
	date = models.DateField("Дата заседания", auto_now_add=True, null=True, blank=True)
	time = models.TimeField("Время заседания")
	subpoena = models.CharField("Повестка", max_length=1000)

class MeetingData(models.Model):
	"""Данные исследования"""
	usersInMeeting = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userInMeeting", null=True, blank=True)
	researchsInMeeting = models.ForeignKey(Research, on_delete=models.CASCADE, related_name="researchId", null=True, blank=True)
	meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="meetingId")

