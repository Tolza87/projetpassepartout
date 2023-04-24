from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Personne

class PersonneUpdateView(UpdateView):
    model = Personne
    fields = '__all__'
    template_name = "personne/personne_update.html"
    success_url = reverse_lazy('personne_list')
