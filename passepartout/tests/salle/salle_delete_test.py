from django.test import TestCase
from django.urls import reverse

class SalleDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_salle_delete_page(self):
        response = self.client.get(reverse('salle_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salle/salle_delete.html')