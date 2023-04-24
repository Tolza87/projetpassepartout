from django.test import TestCase
from django.urls import reverse

class PosseseurDeCLefDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_posseseur_de_c_lef_detail_page(self):
        response = self.client.get(reverse('posseseur_de_c_lef_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posseseur_de_c_lef/posseseur_de_c_lef_detail.html')