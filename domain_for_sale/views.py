import account.views

from django.contrib import auth, messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SignupForm
from .models import OfferForm

class SignupView(account.views.SignupView):
    
    form_class = SignupForm
    
    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)
    
    def create_profile(self, form):
        profile = self.created_user.profile
        profile.birthdate = form.cleaned_data["birthdate"]
        profile.save()

class HomeView(CreateView):
	template_name = 'home.html'
	form_class = OfferForm
	message = {
                "level": messages.SUCCESS,
                "text" : u"intention published."
    }
	success_url = reverse_lazy('home')