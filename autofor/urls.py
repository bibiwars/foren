from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('list.urls')),
    url(r'^', include('analysis.urls')),
    url(r'^', include('disk.urls')),
    url(r'^', include('network.urls')),
    url(r'^', include('manager.urls')),
    
]+ static(settings.MEMORY_IMG_URL, document_root = settings.MEMORY_IMG_PATH) + static(settings.FILE_URL, document_root = settings.FILE_PATH)
