from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base_page, name='base_page'),
    url(r'^accounts/$', views.create_account, name='create_account'),
    url(r'^accounts/(?P<account_id>\d+)/$', views.create_charge, name='create_charge' ),
]