from django.test import TestCase
from django.urls import reverse

class PersonneCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_personne_create_page(self):
        response = self.client.get(reverse('personne_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personne/personne_create.html')