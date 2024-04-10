from django.test import TestCase
from mnemo_api.models.bio_content import BioContent
from mnemo_api.models.diary_entry import DiaryEntry
from mnemo_api.models.image import Image

class BioContentModelTest(TestCase):
    def setUp(self):
        self.diary_entry = DiaryEntry.objects.create(entity_name='test_entity', content='test_content')
        self.image = Image.objects.create(src='test_src', alt='test_alt')

    def test_bio_content_creation(self):
        bio_content = BioContent.objects.create(
            entity_name='test_entity',
            diary_entry=self.diary_entry,
            entity_summary='test_summary',
            date_month='test_date_month'
        )
        bio_content.images.add(self.image)

        self.assertEqual(bio_content.entity_name, 'test_entity')
        self.assertEqual(bio_content.diary_entry, self.diary_entry)
        self.assertEqual(bio_content.entity_summary, 'test_summary')
        self.assertEqual(bio_content.date_month, 'test_date_month')
        self.assertIn(self.image, bio_content.images.all())