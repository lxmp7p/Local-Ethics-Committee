# Generated by Django 3.1.7 on 2021-09-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchManager', '0006_auto_20210921_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='acceptedOnMeeting',
            field=models.BooleanField(default=False, verbose_name='Принято на заседании'),
        ),
    ]
