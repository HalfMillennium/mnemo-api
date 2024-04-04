from django.db import models
from graphene_django import DjangoObjectType
from .bio_content import BioContent

'''
DiaryEntry
- Has One-to-One relationship with BioContent
'''
class DiaryEntry(models.Model):
    entity_name = models.CharField(max_length=100, primary_key=True)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    content = models.TextField()
    bio_content = models.OneToOneField(BioContent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.entity_name} : {self.content}'

class DiaryEntryType(DjangoObjectType):
    class Meta:
        model = DiaryEntry
        fields = ("entity_name", "date", "time", "content")