from django.test import TestCase
from django.urls import reverse

class SalleDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_salle_detail_page(self):
        response = self.client.get(reverse('salle_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salle/salle_detail.html')