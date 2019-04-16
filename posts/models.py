from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)

    def __str__(self):
        return self.content
        
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file =  ProcessedImageField(
                upload_to='posts/images',
                processors=[ResizeToFill(600, 600)],
                format='JPEG',
                options={'quality': 90},
            )

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content