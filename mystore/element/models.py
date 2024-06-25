from django.db import models

# Create your models here.
class Base(models.Model): #Se debe colocar en singular
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title