from django.db import models
from graphene_django import DjangoObjectType

'''
Image
- Should have Many-to-Many relationship with DiaryEntry
'''
class Image(models.Model):
    class Meta:
        app_label = 'core'

    entity_name = models.TextField()
    date_month = models.CharField(max_length=50)
    src = models.TextField()
    alt = models.TextField()

    def __str__(self):
        return self.src

class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = ("entity_name", "date_month", "src", "alt")
