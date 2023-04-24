from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Pouvoir

class PouvoirUpdateView(UpdateView):
    model = Pouvoir
    fields = '__all__'
    template_name = "pouvoir/pouvoir_update.html"
    success_url = reverse_lazy('pouvoir_list')
