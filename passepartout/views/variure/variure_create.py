from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Variure

class VariureCreateView(CreateView):
    model = Variure
    fields = '__all__'
    template_name = "variure/variure_create.html"
    success_url = reverse_lazy('variure_list')
