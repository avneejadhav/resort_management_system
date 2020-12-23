from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content =RichTextField(blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='like_post')

    def __str__(self):
        return self.title

    def number_of_likes(self):
    	return self.likes.count()    

    def get_absolute_url(self):
        return reverse('blog')