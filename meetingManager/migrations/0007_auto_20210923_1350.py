# Generated by Django 3.1.7 on 2021-09-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingManager', '0006_auto_20210923_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата заседания'),
        ),
    ]
