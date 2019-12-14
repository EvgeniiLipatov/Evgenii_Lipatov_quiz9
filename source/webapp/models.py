from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Image(models.Model):
    photo = models.ImageField(upload_to='gallery_images', null=False, blank=False, verbose_name='Photo')
    sign = models.TextField(max_length=200, null=False, blank=False, verbose_name="Subscription")
    likenum = models.IntegerField(null=False, blank=False, default=0, verbose_name="Like quantity")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    userlike = models.ManyToManyField(User, through='webapp.Like',  blank=True, verbose_name='userslike')


class Comment(models.Model):
    text = models.TextField(max_length=1000,null=False, blank=False, verbose_name="text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='author')
    photo = models.ForeignKey('Image', on_delete=models.CASCADE, related_name="comments")

class Like(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True, verbose_name='photo', related_name='photolikes')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, verbose_name='photo', related_name='userlikes')