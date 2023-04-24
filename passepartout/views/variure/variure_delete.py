from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Variure

class VariureDeleteView(DeleteView):
    model = Variure
    template_name = "variure/variure_delete.html"
    success_url = reverse_lazy('variure_list')