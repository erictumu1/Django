from django.db import models

# Create your models here.
class Cars(models.Model):
    car_name = models.CharField(max_length=40)
    car_model = models.CharField(max_length=40)
    car_year = models.IntegerField()
    car_price = models.IntegerField()
    
    def __str__(self):
        return (f"No{self.id}: A {self.car_year} {self.car_name} {self.car_model} is available at ${self.car_price} per week")