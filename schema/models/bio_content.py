from django.db import models
from graphene_django import DjangoObjectType
from .diary_entry import DiaryEntry
from .image import Image

'''
BioContent
- Has One-to-One relationship with DiaryEntry
- Has Many-to-Many relationship with Image
'''
class BioContent(models.Model):
    entity_name = models.CharField(max_length=100, primary_key=True)
    diary_entry = models.OneToOneField(DiaryEntry, on_delete=models.CASCADE)
    entity_summary = models.TextField()
    # Field is blank because it is optional
    images = models.ManyToManyField(Image, blank=True)
    date_month = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.entity_name} : {self.entity_summary}'
    
class BioContentType(DjangoObjectType):
    class Meta:
        model = BioContent
        fields = ("entity_name", "diary_entry", "entity_summary", "images", "date_month")