from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    name = models.TextField('Роль',)
    def __str__(self):
        return self.name


# Create your models here.
class User(AbstractUser):
    username = models.EmailField(
        _('Email'),
        max_length=150,
        unique=True,
        help_text=_(''),
        error_messages={
            'unique': _("Пользователь с таким Email уже существует."),
        },
    )
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=150)
    middle_name = models.CharField('Отчество', max_length=30)
    #email = models.EmailField('Почта')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role', null=True, blank=True, default=7, verbose_name='Роль')
    #phone_number = models.CharField('Номер телефона', max_length=17, null=True, blank=True)
    #birth_date = models.DateField('Дата рождения', null=True, max_length=10)
    password = models.CharField('Пароль', max_length=150)
    registration_accepted = models.CharField('Подтвердить регистрацию',max_length=10)
    #sex = models.CharField('Пол', max_length=30)

    # class Meta(object):
    #     unique_together = ('email',)
    #     db_table = "Users"

    # def __unicode__(self):
    #     return self.username