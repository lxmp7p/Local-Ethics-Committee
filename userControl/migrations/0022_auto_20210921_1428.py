# Generated by Django 3.1.7 on 2021-09-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0021_auto_20210921_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(error_messages={'unique': 'Пользователь с таким Email уже существует.'}, help_text='', max_length=150, unique=True, verbose_name='username'),
        ),
    ]
