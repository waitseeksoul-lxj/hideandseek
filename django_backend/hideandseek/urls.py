from django.conf.urls.defaults import *
from hideandseek.has.views import HView

from django.contrib import admin

admin.autodiscover()

h = HView()
urlpatterns = patterns('',
    (r'^admin/(.*)',admin.site.root),
    (r'^backend/testjson/(.*)',h.gview,{'view':'testjson'}),
)
