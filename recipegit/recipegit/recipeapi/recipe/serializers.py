from django.contrib.auth.models import User
from rest_framework import serializers

from recipe.models import Recipe

from recipe.models import RatingAndReview
from rest_framework.permissions import IsAuthenticated


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','name','cuisine','meal_type','ingredients','created_at','updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    permission_classes=[IsAuthenticated]
    class Meta:
        model=RatingAndReview
        fields=['recipe_id','user','rating','comment','created_at','updated_at']


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','password']

    def create(self,validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u