from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from appli.models import Pouvoir

class PouvoirDeleteView(DeleteView):
    model = Pouvoir
    template_name = "pouvoir/pouvoir_delete.html"
    success_url = reverse_lazy('pouvoir_list')