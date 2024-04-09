from django.db import models

'''
Image
- Should have Many-to-Many relationship with DiaryEntry
'''
class Image(models.Model):
    class Meta:
        app_label = 'mnemo_api'

    entity_name = models.CharField(max_length=100)
    date_month = models.CharField(max_length=50)
    src = models.TextField()
    alt = models.TextField()

    def __str__(self):
        return self.src
