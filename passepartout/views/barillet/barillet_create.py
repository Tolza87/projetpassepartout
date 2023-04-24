from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from appli.models import Barillet

class BarilletCreateView(CreateView):
    model = Barillet
    fields = '__all__'
    template_name = "barillet/barillet_create.html"
    success_url = reverse_lazy('barillet_list')
