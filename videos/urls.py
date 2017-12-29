from django.conf.urls import url

from videos.views import videoloop, getvideolist, videoloopbytv, getmediadetailsbytvid, getlistofimages, imageloop

app_name='videos'

urlpatterns = [
    url(r'^$', videoloop, name='videoloop' ),
    url(r'^videolist/$', getvideolist, name='videolist'),
    url(r'^imagelist/$', getlistofimages, name='imagelist'),
    url(r'^imageloop/$', imageloop, name='imageloop'),
    url(r'^tv/(?P<tvid>[a-zA-Z0-9-_]+)$', videoloopbytv, name='videoloopbytv'),
    url(r'^mediabytv:(?P<tvid>[a-zA-Z0-9-_]+)$', getmediadetailsbytvid, name='mediabytv')
]