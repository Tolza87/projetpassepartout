from django.test import TestCase
from django.urls import reverse

class UtilisateurCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_utilisateur_create_page(self):
        response = self.client.get(reverse('utilisateur_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'utilisateur/utilisateur_create.html')