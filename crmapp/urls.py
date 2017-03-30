from django.conf.urls import include, url
from django.contrib import admin
from marketing.views import HomePage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name='home'),
]

