from django.contrib import admin
from .models.image import Image
from .models.diary_entry import DiaryEntry
from .models.bio_content import BioContent

admin.site.register(Image)
admin.site.register(DiaryEntry)
admin.site.register(BioContent)