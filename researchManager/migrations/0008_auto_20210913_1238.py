# Generated by Django 3.1.7 on 2021-09-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchManager', '0007_alter_information_research'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='information',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='researh',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
