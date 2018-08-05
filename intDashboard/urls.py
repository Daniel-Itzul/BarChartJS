from django.conf.urls import url

from .views import intChart, homeView

urlpatterns = [
    url(r'^$', homeView.as_view(), name='home'),
    url(r'^chart/$', intChart.as_view(), name='chart'),
]