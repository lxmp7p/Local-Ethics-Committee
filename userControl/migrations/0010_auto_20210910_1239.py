# Generated by Django 3.2 on 2021-09-10 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0009_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='Роль',
            field=models.ForeignKey(blank=True, default=7, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='userControl.role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(error_messages={'unique': 'Пользователь с таким Email уже существует.'}, help_text='', max_length=150, unique=True, verbose_name='Email'),
        ),
    ]
