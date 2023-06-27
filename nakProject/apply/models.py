from django.db import models
# create를 post로 작성함..
# Create your models here.
class apply(models.Model):
    name = models.CharField(max_length=50, verbose_name='이름')
    number = models.CharField(max_length=20, verbose_name='전화번호')
    instrument = models.CharField(max_length=50, verbose_name='악기', default="")
    link = models.CharField(max_length=150, verbose_name='링크')
    body = models.TextField(verbose_name="자기소개 및 지원동기", default="")
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.number