from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Salle

class SalleCreateView(CreateView):
    model = Salle
    fields = '__all__'
    template_name = "salle/salle_create.html"
    success_url = reverse_lazy('salle_list')
