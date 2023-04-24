from django.test import TestCase
from django.urls import reverse

class PersonneDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_personne_detail_page(self):
        response = self.client.get(reverse('personne_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personne/personne_detail.html')