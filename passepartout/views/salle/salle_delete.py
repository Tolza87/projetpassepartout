from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Salle

class SalleDeleteView(DeleteView):
    model = Salle
    template_name = "salle/salle_delete.html"
    success_url = reverse_lazy('salle_list')