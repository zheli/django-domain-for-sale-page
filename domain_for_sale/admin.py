from django.contrib import admin

from .models import Offer

# Re-register UserAdmin
admin.site.register(Offer)