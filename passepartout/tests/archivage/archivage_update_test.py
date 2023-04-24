from django.test import TestCase
from django.urls import reverse

class ArchivageUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_archivage_update_page(self):
        response = self.client.get(reverse('archivage_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archivage/archivage_update.html')