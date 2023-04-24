from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Appartenir

class AppartenirUpdateView(UpdateView):
    model = Appartenir
    fields = '__all__'
    template_name = "appartenir/appartenir_update.html"
    success_url = reverse_lazy('appartenir_list')
