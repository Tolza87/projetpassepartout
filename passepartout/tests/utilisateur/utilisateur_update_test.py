from django.test import TestCase
from django.urls import reverse

class UtilisateurUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_utilisateur_update_page(self):
        response = self.client.get(reverse('utilisateur_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'utilisateur/utilisateur_update.html')