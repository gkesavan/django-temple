from django.conf.urls import url

from donors.views import getdonorstoday

app_name='donors'

urlpatterns = [
    url(r'^donorstoday/$', getdonorstoday, name='donorstoday')
]
