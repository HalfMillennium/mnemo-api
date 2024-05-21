import graphene
from graphene import relay
import random
from django.db import transaction
from datetime import date, datetime
from asyncio import run
from graphql_relay import from_global_id
from mnemo_api.models.image import Image
from mnemo_api.models.diary_entry import DiaryEntry
from mnemo_api.models.types.diary_entry_type import DiaryEntryType
from mnemo_api.models.types.bio_content_type import BioContentType
from mnemo_api.models.bio_content import BioContent
from mnemo_api.mnemo_logic.server import MnemoService
    
class CreateDiaryEntryAndBioContentMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)
        time_of_writing = graphene.String(required=True)

    diary_entry = graphene.Field(DiaryEntryType)
    bio_content = graphene.Field(BioContentType)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, entity_name, time_of_writing):
        current_date = date.today().strftime('%Y-%m-%d')
        current_date_month = current_date[:7]
        mnemo_service = MnemoService()
        diary_entry = DiaryEntry.objects.filter(entity_name=entity_name, date=current_date).first()
        if(not diary_entry):
            # Otherwise generate new entry
            content = run(mnemo_service.fetch_diary_entry(entity_name))
            diary_entry = DiaryEntry.objects.create(entity_name=entity_name, date=current_date, time=time_of_writing, content=content)

        bio_content = BioContent.objects.filter(entity_name=entity_name, date_month=current_date_month).first()
        if(bio_content):
            if(diary_entry.bio_content is None):
                diary_entry.bio_content = bio_content
            diary_entry.save()
            return CreateDiaryEntryAndBioContentMutation(diary_entry=diary_entry, bio_content=bio_content)
        
        # Otherwise generate new bio content (including images and summary)
        images_list = run(mnemo_service.fetch_entity_images(entity_name))
        image_objects = []
        for img_data in images_list:
            image = Image.objects.create(entity_name=entity_name, date_month=current_date_month, src=img_data["src"], alt=img_data["alt"])
            image_objects.append(image)
        summary = run(mnemo_service.fetch_entity_summary(entity_name))
        bio_content = BioContent.objects.create(entity_name=entity_name, entity_summary=summary, diary_entry=diary_entry, date_month=current_date_month)
        bio_content.images.add(*image_objects)
        diary_entry.bio_content = bio_content
        diary_entry.save()

        return CreateDiaryEntryAndBioContentMutation(diary_entry=diary_entry, bio_content=bio_content)
    
class DeleteDiaryEntryMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, entity_name):
        entry = DiaryEntry.objects.filter(entity_name=entity_name).first()
        if(entry):
            entry.delete()
        return DeleteDiaryEntryMutation()

class Mutation(graphene.ObjectType):
    create_diary_entry_and_bio_content = CreateDiaryEntryAndBioContentMutation.Field()

class Query(graphene.ObjectType):
    all_diary_entries = graphene.List(DiaryEntryType)
    all_bio_contents = graphene.List(BioContentType)

    def resolve_all_diary_entries(self, info):
        return DiaryEntry.objects.all()

    def resolve_all_bio_contents(self, info):
        return BioContent.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)