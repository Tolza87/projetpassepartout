from django.test import TestCase
from django.urls import reverse

class RolesCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_roles_create_page(self):
        response = self.client.get(reverse('roles_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'roles/roles_create.html')