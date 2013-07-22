from django.conf.urls import patterns, include, url

import book.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', book.views.ListAccountView.as_view(),
		name = 'accounts-list',),
	url(r'^new$', book.views.CreateAccountView.as_view(),
		name = 'accounts-new',),
    # Examples:
    # url(r'^$', 'BookSmpl.views.home', name='home'),
    # url(r'^BookSmpl/', include('BookSmpl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
