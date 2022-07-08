from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("silk/", include("silk.urls", namespace="silk")),
    path("", include("wantads.urls", namespace="want_ad")),
    path("category/", include("categories.urls")),
]
if settings.DEBUG:
    # ADD ROOT MEDIA FILES
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
