from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Batiment

class BatimentCreateView(CreateView):
    model = Batiment
    fields = '__all__'
    template_name = "batiment/batiment_create.html"
    success_url = reverse_lazy('batiment_list')
