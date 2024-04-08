from graphene_django import DjangoObjectType
from graphene import Field
from ..bio_content import BioContent

class BioContentType(DjangoObjectType):
    diary_entry = Field('mnemo_api.models.types.diary_entry_type.DiaryEntryType', required=False)
    class Meta:
        model = BioContent
        fields = ("entity_name", "entity_summary", "date_month", "images", "diary_entry")