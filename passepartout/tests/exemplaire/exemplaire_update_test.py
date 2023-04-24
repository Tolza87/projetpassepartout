from django.test import TestCase
from django.urls import reverse

class ExemplaireUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_exemplaire_update_page(self):
        response = self.client.get(reverse('exemplaire_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exemplaire/exemplaire_update.html')