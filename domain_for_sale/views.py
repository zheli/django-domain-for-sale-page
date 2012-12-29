from django.contrib import auth, messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from .models import OfferForm

class HomeView(CreateView):
    template_name = 'home.html'
    form_class = OfferForm
    message = {
                "level": messages.SUCCESS,
                "text" : u"Thanks for your interests! We will contact you soon!"
    }
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        messages.add_message(
                self.request,
                self.message['level'],
                self.message['text']
        )
        return super(HomeView, self).form_valid(form)