from django.test import TestCase
from django.urls import reverse

class ArchivageCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_archivage_create_page(self):
        response = self.client.get(reverse('archivage_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archivage/archivage_create.html')