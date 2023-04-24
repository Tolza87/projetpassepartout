from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from appli.models import Variure

class VariureUpdateView(UpdateView):
    model = Variure
    fields = '__all__'
    template_name = "variure/variure_update.html"
    success_url = reverse_lazy('variure_list')
