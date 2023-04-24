from django.test import TestCase
from django.urls import reverse

class TypeExemplaireCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_type_exemplaire_create_page(self):
        response = self.client.get(reverse('type_exemplaire_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'type_exemplaire/type_exemplaire_create.html')