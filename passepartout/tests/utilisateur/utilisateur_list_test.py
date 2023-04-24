from django.test import TestCase
from django.urls import reverse

class UtilisateurListTestCase(TestCase):
    def setUp(self):
        pass

    def test_utilisateur_list_page(self):
        response = self.client.get(reverse('utilisateur_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'utilisateur/utilisateur_list.html')