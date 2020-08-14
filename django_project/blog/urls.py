from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(),
         name='blog-post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(),
         name='blog-post-delete'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-post-create'),
    path('about/', views.about, name='blog-about'),
]
