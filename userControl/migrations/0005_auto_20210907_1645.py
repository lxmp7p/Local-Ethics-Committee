# Generated by Django 3.2 on 2021-09-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0004_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
