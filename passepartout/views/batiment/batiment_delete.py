from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Batiment

class BatimentDeleteView(DeleteView):
    model = Batiment
    template_name = "batiment/batiment_delete.html"
    success_url = reverse_lazy('batiment_list')