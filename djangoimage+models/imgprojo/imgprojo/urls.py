# image_upload_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
   path('upload/', views.media_upload, name='media_upload'),
    path('display/', views.display_media, name='display_media'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)