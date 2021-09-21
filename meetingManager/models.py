from django.db import models
from django.conf import settings
# Create your models here.


class Meeting(models.Model):
	"""Исследования"""
	date = models.DateTimeField("Дата загрузки в систему", auto_now_add=True, null=True, blank=True)
	

class MeetingData(models.Model):
	"""Данные исследования"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userInMeeting", null=True, blank=True)
	research = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="researchInMeeting", null=True, blank=True)
	meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

