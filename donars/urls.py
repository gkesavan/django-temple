from django.conf.urls import url

from donars.views import getdonarstoday

app_name='donars'

urlpatterns = [
    url(r'^donarstoday/$', getdonarstoday, name='getDonars'),
]
