from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Exemplaire

class ExemplaireDeleteView(DeleteView):
    model = Exemplaire
    template_name = "exemplaire/exemplaire_delete.html"
    success_url = reverse_lazy('exemplaire_list')