from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Ouvre

class OuvreCreateView(CreateView):
    model = Ouvre
    fields = '__all__'
    template_name = "ouvre/ouvre_create.html"
    success_url = reverse_lazy('ouvre_list')
