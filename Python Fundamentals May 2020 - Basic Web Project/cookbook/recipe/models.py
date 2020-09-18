from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=90)

    def __str__(self):
        return self.title