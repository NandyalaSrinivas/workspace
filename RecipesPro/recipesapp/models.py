from django.db import models


class RecipesName(models.Model):
    recipe = models.CharField(max_length=200)
    items = models.CharField(max_length=200)
    making = models.TextField()
