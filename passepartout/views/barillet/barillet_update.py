from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Barillet

class BarilletUpdateView(UpdateView):
    model = Barillet
    fields = '__all__'
    template_name = "barillet/barillet_update.html"
    success_url = reverse_lazy('barillet_list')
