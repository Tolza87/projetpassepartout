from django.test import TestCase
from django.urls import reverse

class PouvoirUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_pouvoir_update_page(self):
        response = self.client.get(reverse('pouvoir_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pouvoir/pouvoir_update.html')