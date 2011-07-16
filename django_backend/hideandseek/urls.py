from django.conf.urls.defaults import *
import hideandseek.has

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)',admin.site.root),
)
