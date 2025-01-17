from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)

   def __str__(self):
       return self.title
   
class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default=1)

   def __str__(self):
       return self.content


class LastAccessed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='last_accessed')
    accessed_at = models.DateTimeField(auto_now=True)