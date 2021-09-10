# Generated by Django 3.2 on 2021-09-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, help_text='', max_length=150, unique=True, verbose_name='username'),
        ),
    ]