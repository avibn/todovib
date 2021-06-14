from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('src.apps.home.urls')),
    path('list/<int:list_id>/', include('src.apps.list.urls')),
    path('admin/', admin.site.urls),
]
