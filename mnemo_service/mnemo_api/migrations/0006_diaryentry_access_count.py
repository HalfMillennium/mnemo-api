# Generated by Django 5.0.4 on 2024-04-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnemo_api', '0005_alter_diaryentry_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryentry',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
    ]
