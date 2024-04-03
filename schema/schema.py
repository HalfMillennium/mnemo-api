import graphene
from graphene import relay
from graphql_relay import from_global_id
from .models import Image, ImageType, DiaryEntry, DiaryEntryType
from ..service.servce import MnemoService
'''
class Query(graphene.ObjectType):
    all_images = graphene.List(ImageType)
    all_diary_entries = graphene.List(DiaryEntryType)
    diary_entry_from_name = graphene.Field(DiaryEntryType, name=graphene.String(required=True))

    def resolve_all_images(root, info):
        return Image.objects.all()

    def resolve_all_diary_entries(root, info):
        return DiaryEntry.objects.all()

    def resolve_diary_entry_from_name(root, info, name):
        try:
            return DiaryEntry.objects.get(name=name)
        except:
            # instead, generate a new diary entry
            return None
'''

class CreateDiaryEntryMutation(relay.ClientIDMutation):
    class Input:
        entity_name = graphene.String(required=True)
        date = graphene.String(requried=True)
        id = graphene.ID()

    # Class attributes define the response of the mutation
    diary_entry = graphene.Field(DiaryEntryType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, entity_name, date, id):

        diary_entry = DiaryEntry.objects.get(name, date)

        if(not diary_entry):
            '''
            Otherwise generate new entry
            GraphQL uses a thread pool, so each request already runs asynchronously
            '''
            mnemo_service = MnemoService()
            content = mnemo_service.fetch_diary_entry(entity_name)
            return CreateDiaryEntryMutation(diary_entry=diary_entry)

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

schema = graphene.Schema(query=Query, mutation=Mutation)