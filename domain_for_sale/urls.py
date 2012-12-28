from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from .views import SignupView, HomeView


urlpatterns = patterns("",
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
