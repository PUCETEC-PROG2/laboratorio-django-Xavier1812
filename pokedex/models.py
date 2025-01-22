from django.db import models
from datetime import date

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='trainer_images', null=True, blank=True, default='trainer_images/default.png')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False) #Para VARCHAR
    POKEMON_TYPES = [
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Electrico'),
        ('D', 'Dragon'),
    ]
    type = models.CharField(max_length=30, null=False, choices=POKEMON_TYPES)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=7, decimal_places=2)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to='pokemon_images')
    
    def __str__(self):
        return self.name