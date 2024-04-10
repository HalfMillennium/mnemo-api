from django.test import TestCase
from mnemo_api.models.diary_entry import DiaryEntry
from mnemo_api.models.bio_content import BioContent

class DiaryEntryModelTest(TestCase):
    def setUp(self):
        self.bio_content = BioContent.objects.create(entity_name='test_entity', entity_summary='test_summary')

    def test_diary_entry_creation(self):
        diary_entry = DiaryEntry.objects.create(
            entity_name='test_entity',
            date='test_date',
            time='test_time',
            content='test_content',
            bio_content=self.bio_content
        )

        self.assertEqual(diary_entry.entity_name, 'test_entity')
        self.assertEqual(diary_entry.date, 'test_date')
        self.assertEqual(diary_entry.time, 'test_time')
        self.assertEqual(diary_entry.content, 'test_content')
        self.assertEqual(diary_entry.bio_content, self.bio_content)

    def test_diary_entry_string_representation(self):
        diary_entry = DiaryEntry.objects.create(
            entity_name='test_entity',
            date='test_date',
            time='test_time',
            content='test_content',
            bio_content=self.bio_content
        )

        self.assertEqual(str(diary_entry), 'test_entity : test_content')