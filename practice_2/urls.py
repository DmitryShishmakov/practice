from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^log/(?P<param>([A-z-]*/)*)$', 'pages.views.listing'),
)
