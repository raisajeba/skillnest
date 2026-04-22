from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100,blank = True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    category = models.CharField(max_length = 50 )

    def __str__(self):
        return self.name