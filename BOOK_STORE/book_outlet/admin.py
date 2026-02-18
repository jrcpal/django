from django.contrib import admin

# Register your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField()