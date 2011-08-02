from django.conf.urls.defaults import *
from hideandseek.has.views import HView
from django.contrib import admin

admin.autodiscover()

h = HView()
urlpatterns = patterns('',
    (r'^admin/?$',admin.site.root),
    (r'^test/jsonin/?$',h.gview,{'view':'jsonin'}),
    (r'^test/jsonout/?$',h.gview,{'view':'jsonout'}),
    (r'^test/avgpoints/?$',h.gview,{'view':'avgpoints'}),
)
