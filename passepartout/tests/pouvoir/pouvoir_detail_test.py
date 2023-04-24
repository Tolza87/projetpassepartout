from django.test import TestCase
from django.urls import reverse

class PouvoirDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_pouvoir_detail_page(self):
        response = self.client.get(reverse('pouvoir_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pouvoir/pouvoir_detail.html')