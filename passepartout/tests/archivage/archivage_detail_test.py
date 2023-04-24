from django.test import TestCase
from django.urls import reverse

class ArchivageDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_archivage_detail_page(self):
        response = self.client.get(reverse('archivage_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'archivage/archivage_detail.html')