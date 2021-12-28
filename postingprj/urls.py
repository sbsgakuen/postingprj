from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from postingapp.views import top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name='top'),
    path('postingapp/', include('postingapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
