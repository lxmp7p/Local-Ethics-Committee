# Generated by Django 3.1.7 on 2021-09-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchManager', '0008_auto_20210913_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='researh',
            name='customer',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Заказчик'),
        ),
        migrations.AddField(
            model_name='researh',
            name='customer_contacts',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Контактные данные заказчика'),
        ),
        migrations.AddField(
            model_name='researh',
            name='division',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='researh',
            name='drug_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название препарата'),
        ),
        migrations.AddField(
            model_name='researh',
            name='duration',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания исследования'),
        ),
        migrations.AddField(
            model_name='researh',
            name='executor',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='researh',
            name='main_researcher',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Главвный исследователь'),
        ),
        migrations.AddField(
            model_name='researh',
            name='managers',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Менеджеры'),
        ),
        migrations.AddField(
            model_name='researh',
            name='name_research',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название исследования'),
        ),
        migrations.AddField(
            model_name='researh',
            name='protocol_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название протокола'),
        ),
        migrations.AddField(
            model_name='researh',
            name='protocol_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер протокола'),
        ),
        migrations.AddField(
            model_name='researh',
            name='research_center',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Исследовательский центр'),
        ),
        migrations.AddField(
            model_name='researh',
            name='specialization',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Специализация'),
        ),
        migrations.AddField(
            model_name='researh',
            name='work_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название работы'),
        ),
        migrations.DeleteModel(
            name='Information',
        ),
    ]
