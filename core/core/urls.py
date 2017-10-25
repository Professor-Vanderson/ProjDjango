from django.conf.urls import url
from django.contrib import admin
from ecom.views import *

urlpatterns = [
	url(r'^$',index),
    url(r'^admin/', admin.site.urls),
]
