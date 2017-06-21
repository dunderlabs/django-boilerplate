from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Django admin
    url(r'^admin/', include(admin.site.urls)),
    # Local apps
    url(r'^', include('backend.core.urls', namespace='core')),
]
