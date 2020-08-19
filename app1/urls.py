from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/exp/$', views.submit_exp, name='submit_exp')
]