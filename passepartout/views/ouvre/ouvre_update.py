from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Ouvre

class OuvreUpdateView(UpdateView):
    model = Ouvre
    fields = '__all__'
    template_name = "ouvre/ouvre_update.html"
    success_url = reverse_lazy('ouvre_list')
