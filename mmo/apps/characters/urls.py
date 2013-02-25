from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
import views

urlpatterns = patterns('',
    url(r'^listing/$', login_required(views.CharacterListing.as_view()), name="listing"),
    url(r'^create/$', login_required(views.CharacterCreate.as_view()), name="create"),
    url(r'^view/(?P<id>\d+)/$', views.CharacterView.as_view(), name="view"),
    url(r'^play/(?P<id>\d+)/$', login_required(views.CharacterPlay.as_view()), name="play"),
)
