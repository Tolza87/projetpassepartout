from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Pouvoir

class PouvoirCreateView(CreateView):
    model = Pouvoir
    fields = '__all__'
    template_name = "pouvoir/pouvoir_create.html"
    success_url = reverse_lazy('pouvoir_list')
