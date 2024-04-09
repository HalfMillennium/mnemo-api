from graphene_django import DjangoObjectType
from graphene import Field
from ..diary_entry import DiaryEntry

class DiaryEntryType(DjangoObjectType):
    bio_content = Field('mnemo_api.models.types.bio_content_type.BioContentType', required=False)
    class Meta:
        model = DiaryEntry
        fields = ("entity_name", "date", "time", "content", "bio_content")