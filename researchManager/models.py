from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Research(models.Model):
    """Исследования"""
    type = models.CharField("Тип исследования", max_length=50, null=True, blank=True)
    type_request = models.CharField("Тип заявки", max_length=50, null=True, blank=True)
    owner = models.CharField("ОВНЕР", max_length=50, null=True, blank=True)
    identityCode = models.CharField("Код исследования", max_length=50, null=True, blank=True)
    date_accepted = models.DateField("Дата одобрения", blank=True, null=True)
    date_created = models.DateTimeField("Дата загрузки в систему", auto_now_add=True, null=True, blank=True)
    version = models.CharField("Версия исследования", max_length=50, null=True, blank=True)
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
    research_center = models.CharField("Исследовательский центр", max_length=500, null=True, blank=True)
    customer = models.CharField("Заказчик", max_length=500, null=True, blank=True)
    customer_contacts = models.CharField("Контактные данные заказчика", max_length=500, null=True, blank=True)
    duration = models.DateTimeField("Дата окончания исследования", null=True, blank=True)

    class Meta:
        verbose_name = "Исследование"
        verbose_name_plural = "Исследования"

    def __str__(self):
        return self.protocol_number


class Files(models.Model):
    name = models.CharField("Название документа", max_length=150)
    version = models.CharField("Версия документа", max_length=50, null=True, blank=True)
    date = models.CharField("Дата документа", max_length=50, null=True, blank=True)
    file = models.FileField("Путь к файлу")
    research = models.ForeignKey(Research, on_delete=models.CASCADE, related_name='research_id')


