from django.db import models
class Books(models.Model):
    title = models.CharField("书名",max_length=100,unique=True)
    pub = models.CharField("出版社",max_length=40)
    price = models.DecimalField("定价",max_digits=6,decimal_places=2,default=99)
    market_price = models.DecimalField("零售价",max_digits=6,decimal_places=2,default=9.9)

    def __str__(self):
        return "id:%d,书名:%s,出版社:%s"%(self.id,self.title,self.pub)
# Create your models here.
