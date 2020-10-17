from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
        #run the interactive shell
        #python manage.py shell
        #from blog.models import Post
        #from django.contrib.auth.models import User
        #.modelname_set eg:user.post_set