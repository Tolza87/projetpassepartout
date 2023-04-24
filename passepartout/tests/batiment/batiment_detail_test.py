from django.test import TestCase
from django.urls import reverse

class BatimentDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_batiment_detail_page(self):
        response = self.client.get(reverse('batiment_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'batiment/batiment_detail.html')