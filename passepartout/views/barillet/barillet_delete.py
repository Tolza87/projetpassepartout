from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Barillet

class BarilletDeleteView(DeleteView):
    model = Barillet
    template_name = "barillet/barillet_delete.html"
    success_url = reverse_lazy('barillet_list')