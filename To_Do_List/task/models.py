from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
class Listing(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    EASY = 1
    MEDIUM = 2
    HARD = 3

    PRIORITY_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]
    Priority=models.IntegerField(choices=PRIORITY_CHOICES,default=MEDIUM)
    start_date=models.DateField()
    end_date =models.DateField() 
    role=models.CharField(max_length=1000)
    isActive=models.BooleanField(default=True)
    
    def __str__(self):
        return self.note