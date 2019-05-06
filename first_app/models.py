from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Catagory(models.Model):
    Name=models.CharField(max_length=40)
    def __str__(self):
        return self.Name

class Post(models.Model):
    PostId=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=100)
    Body=models.CharField(max_length=1000000)
    Catagory=models.ForeignKey(Catagory)
    
    def __str__(self):
        return str(self.PostId)

class Comment(models.Model):
    ComId=models.AutoField(primary_key=True)
    Message=models.CharField(max_length=500)
    Email=models.EmailField(max_length=100)
    PostId=models.CharField(max_length=10000)

    def __str__(self):
        return str(self.ComId)