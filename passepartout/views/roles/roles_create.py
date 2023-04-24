from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Roles

class RolesCreateView(CreateView):
    model = Roles
    fields = '__all__'
    template_name = "roles/roles_create.html"
    success_url = reverse_lazy('roles_list')
