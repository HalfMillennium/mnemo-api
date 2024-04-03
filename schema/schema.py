import graphene
from graphene import relay
import random
from datetime import date
from graphql_relay import from_global_id
from .models import Image, ImageType, DiaryEntry, DiaryEntryType
from ..core.service.server import MnemoService

class CreateDiaryEntryMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)
        date = graphene.String(required=True)
        id = graphene.ID()

    # Class attributes define the response of the mutation
    diary_entry = graphene.Field(DiaryEntryType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, entity_name):
        current_date = date.today().strftime('%Y-%m-%d')
        diary_entry = None
        try:
            diary_entry = DiaryEntry.objects.get(entity_name=entity_name, date=current_date)
        except DiaryEntry.DoesNotExist:
            pass
        if(not diary_entry):
            '''
            Otherwise generate new entry
            GraphQL uses a thread pool, so each request already runs asynchronously
            '''
            mnemo_service = MnemoService()
            content = mnemo_service.fetch_diary_entry(entity_name)
            random_time_of_day = f'{random.randint(0, 23)}:{random.randint(0, 59)} EST'

            diary_entry = DiaryEntry.objects.create(entity_name=entity_name, date=current_date, time=random_time_of_day, content=content)
            return CreateDiaryEntryMutation(diary_entry=diary_entry)

        return CreateDiaryEntryMutation(diary_entry=diary_entry)

class CreateEntityImageSetMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)
        date = graphene.String(required=True)

    images = graphene.List(ImageType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, entity_name):
        current_date = date.today().strftime('%m-%d')
        image_set = Image.objects.filter(entity_name=entity_name, date_month=current_date)
        if(image_set):
            return CreateEntityImageSetMutation(images=image_set)
        
        mnemo_service = MnemoService()
        images_list = mnemo_service.fetch_entity_images(entity_name)
        image_objects = []
        for img_data in images_list:
            image = Image.objects.create(entity_name, date_month=current_date, src=img_data["src"], alt=img_data["alt"])
            image_objects.append(image)
        return CreateEntityImageSetMutation(images=image_objects)

class Mutation(graphene.ObjectType):
    create_diary_entry = CreateDiaryEntryMutation.Field()
    create_image_set = CreateEntityImageSetMutation.Field()

schema = graphene.Schema(mutation=Mutation)