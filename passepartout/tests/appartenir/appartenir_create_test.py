from django.test import TestCase
from django.urls import reverse

class AppartenirCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_appartenir_create_page(self):
        response = self.client.get(reverse('appartenir_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appartenir/appartenir_create.html')