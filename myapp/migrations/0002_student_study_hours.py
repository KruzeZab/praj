# Generated by Django 4.2.6 on 2023-10-09 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='study_hours',
            field=models.IntegerField(default=0),
        ),
    ]
