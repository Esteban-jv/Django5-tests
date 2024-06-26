from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

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
    slug = models.CharField(max_length=50, blank=True) #blank=True indica que el contenido puede ser ""

    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    @admin.display(boolean=True)
    def cheap(self):
        return 0 <= self.price < 9.9

    def clean(self): # Este metodo aplica validaciones antes de guardar
        if self.price < 0:
            raise ValidationError("El precio no puede ser menor a 0") # Esta es la excepción en validaciones de Django Admin

    def __str__(self):
        return self.title