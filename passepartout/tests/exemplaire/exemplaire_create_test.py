from django.test import TestCase
from django.urls import reverse

class ExemplaireCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_exemplaire_create_page(self):
        response = self.client.get(reverse('exemplaire_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exemplaire/exemplaire_create.html')