from django.contrib import admin
from django.urls import path, include
from blog import views
from .views import PostListView, PostDetailView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail')
]
