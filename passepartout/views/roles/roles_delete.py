from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Roles

class RolesDeleteView(DeleteView):
    model = Roles
    template_name = "roles/roles_delete.html"
    success_url = reverse_lazy('roles_list')