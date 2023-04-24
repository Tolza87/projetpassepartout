from django.test import TestCase
from django.urls import reverse

class PersonneListTestCase(TestCase):
    def setUp(self):
        pass

    def test_personne_list_page(self):
        response = self.client.get(reverse('personne_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personne/personne_list.html')