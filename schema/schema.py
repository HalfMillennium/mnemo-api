import graphene
from graphene import relay
from graphql_relay import from_global_id
from .models import Image, ImageType, DiaryEntry, DiaryEntryType
from ..core.service import MnemoService

class CreateDiaryEntryMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)
        date = graphene.String(requried=True)
        id = graphene.ID()

    # Class attributes define the response of the mutation
    diary_entry = graphene.Field(DiaryEntryType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, entity_name, date, id):

        diary_entry = DiaryEntry.objects.get(entity_name, date)

        if(not diary_entry):
            '''
            Otherwise generate new entry
            GraphQL uses a thread pool, so each request already runs asynchronously
            '''
            mnemo_service = MnemoService()
            content = mnemo_service.fetch_diary_entry(entity_name)
            return CreateDiaryEntryMutation(diary_entry=content)

        return CreateDiaryEntryMutation(diary_entry)

class CreateEntityImageSetMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)
        date = graphene.String(required=True)
        id = graphene.ID()

    images = graphene.List(ImageType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, entity_name):
        mnemo_service = MnemoService()
        images_list = mnemo_service.fetch_images(entity_name)

        image_objects = []
        for img_data in images_list:
            image = Image.objects.create(src=img_data["src"], alt=img_data["alt"])
            image_objects.append(image)

        return CreateEntityImageSetMutation(images=image_objects)

class Mutation(graphene.ObjectType):
    create_diary_entry = CreateDiaryEntryMutation.Field()
    create_image_set = CreateEntityImageSetMutation.Field()

schema = graphene.Schema(mutation=Mutation)