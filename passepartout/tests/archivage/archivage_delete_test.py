from django.test import TestCase
from django.urls import reverse

class ArchivageDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_archivage_delete_page(self):
        response = self.client.get(reverse('archivage_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archivage/archivage_delete.html')