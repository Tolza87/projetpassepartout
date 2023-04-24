from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Personne

class PersonneDeleteView(DeleteView):
    model = Personne
    template_name = "personne/personne_delete.html"
    success_url = reverse_lazy('personne_list')