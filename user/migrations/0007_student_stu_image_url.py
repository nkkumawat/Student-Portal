# Generated by Django 2.0.2 on 2018-02-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180214_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_image_url',
            field=models.CharField(default='', max_length=300),
        ),
    ]
