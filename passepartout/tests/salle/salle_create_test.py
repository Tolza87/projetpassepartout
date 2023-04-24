from django.test import TestCase
from django.urls import reverse

class SalleCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_salle_create_page(self):
        response = self.client.get(reverse('salle_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salle/salle_create.html')