from django.contrib import admin
from django.urls import path
from .views import index, UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('2/', UserListView.as_view(), name='user'),
]
