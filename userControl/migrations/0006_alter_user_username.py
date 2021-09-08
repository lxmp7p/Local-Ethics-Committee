# Generated by Django 3.2 on 2021-09-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0005_auto_20210907_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that email already exists.'}, help_text='', max_length=150, unique=True, verbose_name='username'),
        ),
    ]
