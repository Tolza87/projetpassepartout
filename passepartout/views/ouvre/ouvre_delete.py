from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Ouvre

class OuvreDeleteView(DeleteView):
    model = Ouvre
    template_name = "ouvre/ouvre_delete.html"
    success_url = reverse_lazy('ouvre_list')