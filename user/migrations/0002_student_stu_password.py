# Generated by Django 2.0.2 on 2018-02-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_password',
            field=models.CharField(default='', max_length=300),
        ),
    ]
