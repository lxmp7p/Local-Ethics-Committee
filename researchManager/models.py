from django.db import models
from django.conf import settings
from datetime import date
# Create your models here.
class Research(models.Model):
    """Исследования"""
    type = models.CharField("Тип исследования", max_length=50, null=True, blank=True)
    type_request = models.CharField("Тип заявки", max_length=50, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    identityCode = models.CharField("Код исследования", max_length=50, null=True, blank=True)
    date_accepted = models.DateField("Дата одобрения", blank=True, null=True, default="2021-05-05")
    date_created = models.DateTimeField("Дата загрузки в систему", auto_now_add=True, null=True, blank=True)
    protocol_number = models.CharField("Номер протокола", max_length=50, null=True, blank=True)
    protocol_name = models.CharField("Название протокола", max_length=500, null=True, blank=True)
    work_name = models.CharField("Название работы", max_length=500, null=True, blank=True)
    division = models.CharField("Подразделение", max_length=500, null=True, blank=True)
    executor = models.CharField("Исполнитель", max_length=500, null=True, blank=True)
    specialization = models.CharField("Специализация", max_length=500, null=True, blank=True)
    managers = models.CharField("Менеджеры", max_length=500, null=True, blank=True)
    name_research = models.CharField("Название исследования", max_length=500, null=True, blank=True)
    drug_name = models.CharField("Название препарата", max_length=500, null=True, blank=True)
    main_researcher = models.CharField("Главный исследователь", max_length=500, null=True, blank=True)
    research_center = models.CharField("Исследовательский центр", max_length=500, null=True, blank=True)
    customer = models.CharField("Заказчик", max_length=500, null=True, blank=True)
    customer_contacts = models.CharField("Контактные данные заказчика", max_length=500, null=True, blank=True)
    duration = models.CharField("Срок проведения исследования", max_length=150, null=True, blank=True)
    version = models.IntegerField("Версия", null=True, blank=True)
    addedOnMeeting = models.BooleanField("Добавленно на заседании", default=False)
    

    class Meta:
        verbose_name = "Исследование"
        verbose_name_plural = "Исследования"

    def __str__(self, MAX_LENGTH=70):
        MAX_LENGTH = 70
        if self.type == "clinicalResearch":
            name = self.protocol_name
        if self.type == "preclinicalResearch":
            name = self.work_name
        if self.type == "initiativeResearch":
            name = self.name_research
        if self.type == "dissertationWorksList":
            name = self.work_name
        if len(name) > MAX_LENGTH:
            return name[:MAX_LENGTH] + '...'
        else:
            return name

    def getType(self):
        if self.type == "clinicalResearch":
            return "Клиническое исследование"
        if self.type == "preclinicalResearch":
            return "Доклиническое исследование"
        if self.type == "initiativeResearch":
            return "Инициативное исследование"
        if self.type == "dissertationWorksList":
            return "Диссертационная работа"

    def getDescription(self):
        if self.type == "clinicalResearch":
            return self.protocol_name
        if self.type == "preclinicalResearch":
            return self.work_name
        if self.type == "initiativeResearch":
            return self.name_research
        if self.type == "dissertationWorksList":
            return self.work_name

    def getTypeRequest(self):
        if self.type == "firstRequest":
            return "Первичная заявка"
        if self.type == "secondRequest":
            return "Вторичная заявка"

    def getSubName(self, MAX_LENGTH=70):
        MAX_LENGTH = 70
        if self.type == "clinicalResearch":
            name = self.protocol_number
        if self.type == "preclinicalResearch":
            name = self.work_name
        if self.type == "initiativeResearch":
            name = self.name_research
        if self.type == "dissertationWorksList":
            name = self.work_name
        if len(name) > MAX_LENGTH:
            return name[:MAX_LENGTH] + '...'
        else:
            return name

class Files(models.Model):
    name = models.CharField("Название документа", max_length=150)
    version = models.CharField("Версия документа", max_length=50, null=True, blank=True)
    date = models.CharField("Дата документа", max_length=50, null=True, blank=True)
    file = models.FileField("Путь к файлу")
    research = models.ForeignKey(Research, on_delete=models.CASCADE, related_name='research_id')


