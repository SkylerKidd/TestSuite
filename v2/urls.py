from django.conf.urls import url

from v2 import views

urlpatterns = [
    url(r'api/plot$', views.api_plot, name='v2_api_plot'),
    url(r'api/plot/list', views.list_plots, name='v2_api_list_plots'),
    url(r'', views.home, name="v2_home")
]
