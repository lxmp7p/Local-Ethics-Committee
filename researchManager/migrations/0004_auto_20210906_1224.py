# Generated by Django 3.2.7 on 2021-09-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchManager', '0003_auto_20210906_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to='researchs/%Y/<function user_directory_path at 0x000000722336EEE0>', verbose_name='Путь к файлу'),
        ),
        migrations.AlterField(
            model_name='researh',
            name='owner',
            field=models.CharField(max_length=50, verbose_name='ОВНЕР'),
        ),
    ]
