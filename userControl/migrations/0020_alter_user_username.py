# Generated by Django 3.2 on 2021-09-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0019_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(error_messages={'unique': 'Пользователь с таким Email уже существует.'}, help_text='', max_length=150, unique=True, verbose_name='username'),
        ),
    ]
