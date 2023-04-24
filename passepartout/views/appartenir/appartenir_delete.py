from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Appartenir

class AppartenirDeleteView(DeleteView):
    model = Appartenir
    template_name = "appartenir/appartenir_delete.html"
    success_url = reverse_lazy('appartenir_list')