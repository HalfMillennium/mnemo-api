import graphene
from graphene import relay
import random
from datetime import date
from graphql_relay import from_global_id
from .models.image import Image, ImageType
from .models.diary_entry import DiaryEntry, DiaryEntryType
from .models.bio_content import BioContent, BioContentType
from ..core.service.server import MnemoService
    
class CreateDiaryEntryAndBioContentMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)

    diary_entry = graphene.Field(DiaryEntryType)
    bio_content = graphene.Field(BioContentType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, entity_name):
        current_date = date.today().strftime('%Y-%m-%d')
        mnemo_service = MnemoService()
        diary_entry = DiaryEntry.objects.filter(entity_name=entity_name, date=current_date)
        if(not diary_entry):
            # Otherwise generate new entry
            content = mnemo_service.fetch_diary_entry(entity_name)
            random_time_of_day = f'{random.randint(0, 23)}:{random.randint(0, 59)} EST'
            diary_entry = DiaryEntry.objects.create(entity_name=entity_name, date=current_date, time=random_time_of_day, content=content)

        bio_content = Image.objects.filter(entity_name=entity_name, date_month=current_date)
        if(bio_content):
            return CreateDiaryEntryAndBioContentMutation(diary_entry=diary_entry, bio_content=bio_content)
        # Otherwise generate new bio content (including images and summary)
        images_list = mnemo_service.fetch_entity_images(entity_name)
        image_objects = []
        for img_data in images_list:
            image = Image.objects.create(entity_name, date_month=current_date, src=img_data["src"], alt=img_data["alt"])
            image_objects.append(image)
        summary = mnemo_service.fetch_entity_summary(entity_name)
        bio_content = BioContent.objects.create(entity_name=entity_name, entity_summary=summary, images=image_objects, diary_entry=diary_entry)

        return CreateDiaryEntryAndBioContentMutation(diary_entry=diary_entry, bio_content=bio_content)

class Mutation(graphene.ObjectType):
    create_diary_entry_and_bio_content = CreateDiaryEntryAndBioContentMutation.Field()

schema = graphene.Schema(mutation=Mutation)