from blog_post.models import BlogPost
from rest_framework import generics
from blog_post import serializers
from account.models import User
from rest_framework import permissions
from blog_post.permissions import IsAuthorOrReadOnly
from blog_post.pagination  import BlogListPagination


#get and create Blog Api
class PostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    pagination_class = BlogListPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



#if you are login you perform put and delete operation in your blog 
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        IsAuthorOrReadOnly]
    