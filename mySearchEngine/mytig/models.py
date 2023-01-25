from django.db import models
from json import JSONEncoder

# Create your models here.
"""
class ProduitEnPromotion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)
"""
        
class Book (models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    releaseDate = models.CharField(max_length=256)
    content = models.TextField()
    
    def __str__(self):
        return f'{self.title} : {self.author} - {self.language} - {self.releaseDate}'