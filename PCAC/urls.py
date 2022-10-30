from django.contrib import admin
from django.urls import path,include
#from django.config import settings
#from django.config.urls.static  import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('APPCAC.urls')),
]# + static(settings.STATIC_URL, documen_root=settings.STATIC_ROOT)
