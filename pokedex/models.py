from django.db import models

# Create your models here.
class Pokemon(models.Model):
    pass
    #Django no necesita un innit
    name = models.CharField(max_length=30, null=False) #Para VARCHAR
    type = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(max_digits=6, decimal_places=4)
    height = models.DecimalField(max_digits=6, decimal_places=4)
    
    def __str__(self):
        return self.name