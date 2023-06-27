from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class sPost(models.Model):
    title = models.CharField(verbose_name="노래제목", max_length=128)
    singer = models.CharField(verbose_name="가수", max_length=128, default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title