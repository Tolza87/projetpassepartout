from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Roles

class RolesUpdateView(UpdateView):
    model = Roles
    fields = '__all__'
    template_name = "roles/roles_update.html"
    success_url = reverse_lazy('roles_list')
