
from django.conf.urls import url
from django.views.generic import RedirectView
from mptt_424_app import views

urlpatterns = [
    url(r'^about/$', views.MpttView.as_view(), name='mptt'),
    url(r'^$', RedirectView.as_view(pattern_name='mptt:mptt'), name='index'),
]
