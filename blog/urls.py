from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('categories/', views.category_list, name='category_list'),
    path('', PostListView.as_view(), name = 'post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name ='post_detail'),
    path('post/create/', PostCreateView.as_view(), name ='post_new'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_confirm_delete'),
    

    
    
]