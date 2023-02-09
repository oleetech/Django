from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
## Add This Line
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = HTMLField() # Change This Line
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
# Create your models here.
