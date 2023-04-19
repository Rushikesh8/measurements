
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/measurement/',include("measurement_app.urls",namespace="measurement_app")),
    path('api/accounts/',include("accounts.urls",namespace="accounts")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
