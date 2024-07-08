from django.db import models
from django.contrib.auth.models import User



class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    tarkibi = models.CharField(max_length=100)
    price = models.IntegerField()
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.IntegerField()

    def __str__(self):
        return self.text