from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

# Create your models here.
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class SkillImage(models.Model):
    skill = models.ForeignKey(Skill, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='skill_pics/')

    def __str__(self):
        return f"Image for {self.skill.name}"
