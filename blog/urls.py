from django.contrib import admin
from django.urls import path
from .views import index, posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('posts.html', posts, name='posts'),
]
