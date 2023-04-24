from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Appartenir

class AppartenirCreateView(CreateView):
    model = Appartenir
    fields = '__all__'
    template_name = "appartenir/appartenir_create.html"
    success_url = reverse_lazy('appartenir_list')
