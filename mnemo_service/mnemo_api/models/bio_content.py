from django.db import models
from .image import Image

'''
BioContent
- Has One-to-One relationship with DiaryEntry
- Has Many-to-Many relationship with Image
'''
class BioContent(models.Model):
    class Meta:
        app_label = 'mnemo_api'

    entity_name = models.CharField(max_length=100, primary_key=True)
    diary_entry = models.OneToOneField('mnemo_api.DiaryEntry', on_delete=models.CASCADE, null=True, blank=True)
    entity_summary = models.TextField()
    # Field is blank because it is optional
    images = models.ManyToManyField(Image, blank=True)
    date_month = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.entity_name} : {self.entity_summary}'