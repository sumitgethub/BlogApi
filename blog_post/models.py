from django.db import models
from account.models import User



#Create Blog Model
class BlogPost(models.Model):
    author = models.ForeignKey(User,max_length=30, on_delete=models.CASCADE,related_name="user_author")
    title = models.TextField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title