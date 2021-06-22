from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # Local apps
    path("", include("backend.core.urls", namespace="core")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
