from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nid/', include('national_id_validator.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
