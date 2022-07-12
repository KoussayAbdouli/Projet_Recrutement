from django.db import models

# Create your models here.

class Appartement(models.Model):
    name = models.CharField(max_length=100)
    prix = models.IntegerField()
    nombre_pieces = models.IntegerField()
    list_cr =  models.CharField(max_length=100)

    def __str__(self):
        return self.name


        
class Prog(models.Model):
    fa= models.IntegerField()
    name= models.CharField(max_length=100)
    year= models.IntegerField()
    price= models.FloatField()
    ##
    appartement_id =  models.ManyToManyField(Appartement)
    ##



