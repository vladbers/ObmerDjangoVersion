from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from ObmerAPP.views import home_page, prepareOption

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('api/json', prepareOption)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
