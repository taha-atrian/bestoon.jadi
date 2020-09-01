from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/exp/$', views.submit_exp, name='submit_exp'),
    url(r'^submit/income/$', views.submit_income, name='submit_income'),
    url(r'^register/$', views.register, name='register'),
]
