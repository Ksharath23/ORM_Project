from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.email

class Hashtag(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    created_by = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self) :
        return self.name
    
class Post(models.Model):
    post_name = models.CharField(max_length=100,blank=True,null=True)
    hashtag = models.ManyToManyField(Hashtag)
    created_by = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    #caption
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.post_name
