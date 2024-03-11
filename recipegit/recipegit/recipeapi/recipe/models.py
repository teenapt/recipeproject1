from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Recipe(models.Model):
    name=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=200)
    meal_type=models.CharField(max_length=300)
    ingredients=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class RatingAndReview(models.Model):
    recipe_id=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipe_id.name
