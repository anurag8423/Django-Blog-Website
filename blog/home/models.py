from django.db import models

class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    shortDesc=models.CharField(max_length=350,default="")
    slug=models.CharField(max_length=100,default="")
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


