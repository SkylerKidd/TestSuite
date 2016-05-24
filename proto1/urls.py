__author__ = 'gautam'

from django.conf.urls import url

from proto1 import views

urlpatterns = [
    url(r'api/plot$', views.api_plot, name='api_plot'),
    url(r'api/plot/list', views.list_plots, name='api_list_plots'),
    url(r'', views.home, name="proto1_home")
]
