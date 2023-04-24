from django.test import TestCase
from django.urls import reverse

class UtilisateurDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_utilisateur_delete_page(self):
        response = self.client.get(reverse('utilisateur_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'utilisateur/utilisateur_delete.html')