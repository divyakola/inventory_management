from django.db import models

# Create your models here.
class Products(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=30)
    pqty=models.IntegerField()
    pdesc=models.TextField()
    pimg=models.ImageField()
    def __str__(self):
        return "%d %s %d %s %s"%(self.pid,self.pname,self.pqty,self.pdesc,self.pimg)