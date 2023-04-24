from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Porte

class PorteUpdateView(UpdateView):
    model = Porte
    fields = '__all__'
    template_name = "porte/porte_update.html"
    success_url = reverse_lazy('porte_list')
