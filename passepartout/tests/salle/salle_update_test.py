from django.test import TestCase
from django.urls import reverse

class SalleUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_salle_update_page(self):
        response = self.client.get(reverse('salle_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salle/salle_update.html')