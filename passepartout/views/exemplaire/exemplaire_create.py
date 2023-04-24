from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Exemplaire

class ExemplaireCreateView(CreateView):
    model = Exemplaire
    fields = '__all__'
    template_name = "exemplaire/exemplaire_create.html"
    success_url = reverse_lazy('exemplaire_list')
