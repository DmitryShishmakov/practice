from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		#url(r'^log/(?P<param>([A-z-]*/)*)$', 'pages.views.listing'),
		url(r'^library/$', 'library.views.books'),
		url(r'^library/books/$', 'library.views.books'),
		url(r'^library/books/(\d+)/$', 'library.views.book'),
		url(r'^library/authors/$', 'library.views.authors'),
		url(r'^library/authors/(\d+)/$', 'library.views.author'),

		url(r'^admin/', include(admin.site.urls)),
)