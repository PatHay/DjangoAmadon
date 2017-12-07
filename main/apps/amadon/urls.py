from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^purchase/(?P<item_id>\d+)', views.purchase),
    url(r'^checkout$', views.checkout)
]