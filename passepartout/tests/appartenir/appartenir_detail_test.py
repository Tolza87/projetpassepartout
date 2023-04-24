from django.test import TestCase
from django.urls import reverse

class AppartenirDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_appartenir_detail_page(self):
        response = self.client.get(reverse('appartenir_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appartenir/appartenir_detail.html')