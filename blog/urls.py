from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
   # path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('categories/', views.category_list, name='categories'),
    path('', PostListView.as_view(), name = 'post_list'),
]