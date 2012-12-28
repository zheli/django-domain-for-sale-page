from django.db import models
from django.forms import ModelForm

class Offer(models.Model):
	#name = models.CharField(max_length = 255)
	email = models.EmailField(null=False)
	message = models.TextField(max_length = 2048, null=False)

	def __unicode__(self):
		return self.email

class OfferForm(ModelForm):
    class Meta:
        model = Offer