from django.test import TestCase
from django.urls import reverse

class UtilisateurDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_utilisateur_detail_page(self):
        response = self.client.get(reverse('utilisateur_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'utilisateur/utilisateur_detail.html')