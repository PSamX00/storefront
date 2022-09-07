from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100,null=False)  
    image= models.URLField(max_length=300,null=False)
    stock=models.IntegerField(default=0)
    price= models.IntegerField(default=0)
    discount= models.IntegerField(default=0)
    def __str__(self):
        return "%s %s %s %s" %(self.name, self.stock, self.price,self.discount)