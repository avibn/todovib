from django.urls import path

from .views import *

app_name = 'Home'
urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('list/create/', CreateListView.as_view(), name="create_list"),
]
