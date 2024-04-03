from django.db import models
from graphene_django import DjangoObjectType

'''
Image
- Should have Many-to-Many relationship with DiaryEntry
'''
class Image(models.Model):
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

'''
DiaryEntry
- Has Many-to-Many relationship with Image
'''
class DiaryEntry(models.Model):
    entity_name = models.CharField(max_length=100, primary_key=True)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    content = models.TextField()
    # Field is blank because it is optional
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return f'{self.entity_name} : {self.content}'

class DiaryEntryType(DjangoObjectType):
    class Meta:
        model = DiaryEntry
        fields = ("entity_name", "date", "time", "content")


'''
BioContent
- Has One-to-One relationship with DiaryEntry
'''
class BioContent(models.Model):
    entity_name = models.CharField(max_length=100, primary_key=True)
    diary_entry = models.OneToOneField(DiaryEntry, on_delete=models.CASCADE)
    entity_summary = models.TextField()

    def __str__(self):
        return f'{self.entity_name} : {self.entity_summary}'