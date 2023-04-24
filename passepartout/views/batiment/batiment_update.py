from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Batiment

class BatimentUpdateView(UpdateView):
    model = Batiment
    fields = '__all__'
    template_name = "batiment/batiment_update.html"
    success_url = reverse_lazy('batiment_list')
