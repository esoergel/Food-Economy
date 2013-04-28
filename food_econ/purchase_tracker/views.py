from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Purchase
from .forms import PurchaseForm

class MakePurchase(CreateView):
    form_class = PurchaseForm
    model = Purchase
    template_name = "add_purchase.html"
    success_url = "success/"
    
    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.instance.user = self.request.user
        self.object = form.save()
        return super(MakePurchase, self).form_valid(form)