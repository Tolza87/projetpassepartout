from django.test import TestCase
from django.urls import reverse

class VariureDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_variure_detail_page(self):
        response = self.client.get(reverse('variure_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'variure/variure_detail.html')