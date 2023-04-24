from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Salle

class SalleUpdateView(UpdateView):
    model = Salle
    fields = '__all__'
    template_name = "salle/salle_update.html"
    success_url = reverse_lazy('salle_list')
