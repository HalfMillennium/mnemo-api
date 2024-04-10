from django.test import TestCase
from graphene.test import Client
from mnemo_api.schema import schema
from mnemo_api.models.diary_entry import DiaryEntry
from mnemo_api.models.bio_content import BioContent
from mnemo_api.models.image import Image

class CreateDiaryEntryAndBioContentMutationTest(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_create_diary_entry_and_bio_content(self):
        # Arrange
        entity_name = 'test_entity'
        mutation = f'''
        mutation {{
            createDiaryEntryAndBioContent(input: {{entityName: "{entity_name}"}}) {{
                diaryEntry {{
                    entityName
                    date
                    content
                }}
                bioContent {{
                    entityName
                    entitySummary
                }}
            }}
        }}
        '''

        # Act
        result = self.client.execute(mutation)

        # Assert
        if result is not None and result.get('data') and result['data'].get('createDiaryEntryAndBioContent'):
            self.assertIsNotNone(result['data']['createDiaryEntryAndBioContent'].get('diaryEntry'))
            self.assertIsNotNone(result['data']['createDiaryEntryAndBioContent'].get('bioContent'))
            self.assertEqual(result['data']['createDiaryEntryAndBioContent'].get('diaryEntry', {}).get('entityName'), entity_name)
            self.assertEqual(result['data']['createDiaryEntryAndBioContent'].get('bioContent', {}).get('entityName'), entity_name)
            self.assertIsNotNone(DiaryEntry.objects.filter(entity_name=entity_name).first())
            self.assertIsNotNone(BioContent.objects.filter(entity_name=entity_name).first())
        else:
            self.fail(f"The mutation execution returned None or did not contain the expected keys: {result}")