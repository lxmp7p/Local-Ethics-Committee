from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Researh(models.Model):
    """Исследования"""
    type = models.CharField("Тип исследования", max_length=50)
    type_request = models.CharField("Тип заявки", max_length=50)
    owner = models.CharField("ОВНЕР", max_length=50)
    #owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    identityCode = models.CharField("Код исследования", max_length=50)
    date_accepted = models.DateTimeField("Дата одобрения", blank=True, null=True, default='2021-05-25 11:17:49.353268')
    date_created = models.DateTimeField("Дата загрузки в систему", auto_now_add=True)
    version = models.CharField("Версия исследования", max_length=50)

    class Meta:
        verbose_name = "Исследование"
        verbose_name_plural = "Исследования"


class Files(models.Model):
    name = models.CharField("Название документа", max_length=150)
    version = models.CharField("Версия документа", max_length=50, null=True, blank=True)
    date = models.DateField("Дата документа", null=True, blank=True)
    file = models.FileField("Путь к файлу")
    research = models.ForeignKey(Researh, on_delete=models.CASCADE, related_name='research_id')


class Information(models.Model):
    protocol_number = models.CharField("Номер протокола", max_length=50, null=True, blank=True)
    protocol_name = models.CharField("Название протокола", max_length=500, null=True, blank=True)
    work_name = models.CharField("Название работы", max_length=500, null=True, blank=True)
    division = models.CharField("Подразделение", max_length=500, null=True, blank=True)
    executor = models.CharField("Исполнитель", max_length=500, null=True, blank=True)
    specialization = models.CharField("Специализация", max_length=500, null=True, blank=True)
    managers = models.CharField("Менеджеры", max_length=500, null=True, blank=True)
    name_research = models.CharField("Название исследования", max_length=500, null=True, blank=True)
    drug_name = models.CharField("Название препарата", max_length=500, null=True, blank=True)
    main_researcher = models.CharField("Главвный исследователь", max_length=500, null=True, blank=True)
    #main_researcher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='main_researcher_id')
    research_center = models.CharField("Исследовательский центр", max_length=500, null=True, blank=True)
    customer = models.CharField("Заказчик", max_length=500, null=True, blank=True)
    customer_contacts = models.CharField("Контактные данные заказчика", max_length=500, null=True, blank=True)
    duration = models.DateTimeField("Дата окончания исследования", null=True, blank=True)
    research = models.ForeignKey(Researh, on_delete=models.CASCADE, related_name='info_research_id')

