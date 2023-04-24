from django.test import TestCase
from django.urls import reverse

class RolesUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_roles_update_page(self):
        response = self.client.get(reverse('roles_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roles/roles_update.html')