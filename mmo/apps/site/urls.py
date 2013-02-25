from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomepageView.as_view(), name="homepage"),
    url(r'^register/$', views.RegisterView.as_view(), name="login"),
)
