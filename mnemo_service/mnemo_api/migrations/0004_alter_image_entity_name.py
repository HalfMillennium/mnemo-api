# Generated by Django 5.0.4 on 2024-04-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnemo_api', '0003_alter_biocontent_diary_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='entity_name',
            field=models.CharField(max_length=100),
        ),
    ]