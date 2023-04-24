from django.test import TestCase
from django.urls import reverse

class AppartenirUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_appartenir_update_page(self):
        response = self.client.get(reverse('appartenir_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appartenir/appartenir_update.html')