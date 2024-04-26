from django.db import models

'''
DiaryEntry
- Has One-to-One relationship with BioContent
'''
class DiaryEntry(models.Model):
    class Meta:
        app_label = 'mnemo_api'

    entity_name = models.CharField(max_length=100, primary_key=True)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    bio_content = models.OneToOneField('mnemo_api.BioContent', on_delete=models.CASCADE, null=True, blank=True)
    access_count = models.IntegerField(default=0)

    def increment_access_count(self):
        self.access_count += 1
        self.save()

    def __str__(self):
        return f'{self.entity_name} : {self.content}'