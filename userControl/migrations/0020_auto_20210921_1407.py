# Generated by Django 3.1.7 on 2021-09-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0019_auto_20210920_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(error_messages={'unique': 'Пользователь с таким Email уже существует.'}, help_text='', max_length=150, unique=True, verbose_name='username'),
        ),
    ]