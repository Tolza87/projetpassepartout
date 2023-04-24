from django.test import TestCase
from django.urls import reverse

class PosseseurDeCLefCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_posseseur_de_c_lef_create_page(self):
        response = self.client.get(reverse('posseseur_de_c_lef_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posseseur_de_c_lef/posseseur_de_c_lef_create.html')