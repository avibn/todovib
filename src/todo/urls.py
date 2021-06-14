from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('<int:id>/', include('src.apps.home.urls')),
    path('admin/', admin.site.urls),
]
