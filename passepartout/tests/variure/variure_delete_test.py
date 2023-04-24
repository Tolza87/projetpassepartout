from django.test import TestCase
from django.urls import reverse

class VariureDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_variure_delete_page(self):
        response = self.client.get(reverse('variure_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'variure/variure_delete.html')