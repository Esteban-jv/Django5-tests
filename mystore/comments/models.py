from django.db import models
from element.models import Element

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    posted = models.DateTimeField(auto_now=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, null=True, related_name='comments') #related name nos sirve para declarar una relación inversa hacia comments

    def __str__(self):
        return 'Comment #{}'.format(self.id)