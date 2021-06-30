# Generated by Django 3.2.4 on 2021-06-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20210610_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_requirement',
            field=models.TextField(max_length=1024, verbose_name='职位要求'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='bachelor_school',
            field=models.CharField(blank=True, max_length=135, verbose_name='本科学校'),
        ),
    ]
