from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Porte

class PorteDeleteView(DeleteView):
    model = Porte
    template_name = "porte/porte_delete.html"
    success_url = reverse_lazy('porte_list')