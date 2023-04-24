from django.test import TestCase
from django.urls import reverse

class ExemplaireDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_exemplaire_delete_page(self):
        response = self.client.get(reverse('exemplaire_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exemplaire/exemplaire_delete.html')