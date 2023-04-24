from django.test import TestCase
from django.urls import reverse

class ExemplaireListTestCase(TestCase):
    def setUp(self):
        pass

    def test_exemplaire_list_page(self):
        response = self.client.get(reverse('exemplaire_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exemplaire/exemplaire_list.html')