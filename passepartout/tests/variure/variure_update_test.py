from django.test import TestCase
from django.urls import reverse

class VariureUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_variure_update_page(self):
        response = self.client.get(reverse('variure_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'variure/variure_update.html')