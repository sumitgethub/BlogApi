from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog_post import views

urlpatterns = [

    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)