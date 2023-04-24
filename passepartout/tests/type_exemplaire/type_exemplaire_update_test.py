from django.test import TestCase
from django.urls import reverse

class TypeExemplaireUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_type_exemplaire_update_page(self):
        response = self.client.get(reverse('type_exemplaire_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'type_exemplaire/type_exemplaire_update.html')