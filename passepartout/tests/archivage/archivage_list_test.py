from django.test import TestCase
from django.urls import reverse

class ArchivageListTestCase(TestCase):
    def setUp(self):
        pass

    def test_archivage_list_page(self):
        response = self.client.get(reverse('archivage_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archivage/archivage_list.html')