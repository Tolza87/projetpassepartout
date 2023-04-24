from django.views.generic import ListView

from appli.models import Pouvoir

class PouvoirListView(ListView):
    model = Pouvoir
    template_name = "pouvoir/pouvoir_list.html"
