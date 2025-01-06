from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False) #Para VARCHAR
    type = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(max_digits=6, decimal_places=4)
    height = models.DecimalField(max_digits=7, decimal_places=4)
    
    def __str__(self):
        return self.name

