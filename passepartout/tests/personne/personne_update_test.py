from django.test import TestCase
from django.urls import reverse

class PersonneUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_personne_update_page(self):
        response = self.client.get(reverse('personne_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personne/personne_update.html')