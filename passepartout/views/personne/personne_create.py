from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Personne

class PersonneCreateView(CreateView):
    model = Personne
    fields = '__all__'
    template_name = "personne/personne_create.html"
    success_url = reverse_lazy('personne_list')
