from django.test import TestCase
from django.urls import reverse

class VariureCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_variure_create_page(self):
        response = self.client.get(reverse('variure_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'variure/variure_create.html')