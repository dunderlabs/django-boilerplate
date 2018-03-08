from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # Local apps
    path('', include('backend.core.urls', namespace='core')),
]
