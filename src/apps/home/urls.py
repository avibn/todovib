from django.urls import path

from .views import HomeView

app_name = 'Home'
urlpatterns = [
    path('lol/', HomeView.as_view(), name="index")
]
