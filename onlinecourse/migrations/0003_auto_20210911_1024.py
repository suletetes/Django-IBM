# Generated by Django 3.1.3 on 2021-09-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('onlinecourse', '0002_auto_20210601_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=10),
        ),
    ]
