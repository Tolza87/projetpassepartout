from django.test import TestCase
from django.urls import reverse

class PersonneDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_personne_delete_page(self):
        response = self.client.get(reverse('personne_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personne/personne_delete.html')