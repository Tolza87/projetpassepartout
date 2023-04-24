from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Porte

class PorteCreateView(CreateView):
    model = Porte
    fields = '__all__'
    template_name = "porte/porte_create.html"
    success_url = reverse_lazy('porte_list')
