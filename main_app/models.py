from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
SERVICE = (
  ('I', 'Intonation'),
  ('M', 'Maintenance'),
  ('R', 'Repair')
)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    # guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} ({self.id})'
    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})



class Guitar(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  #could use date here but 
  year = models.IntegerField()
  cost = models.IntegerField()
  accessories = models.ManyToManyField(Accessory)
  
  def __str__(self):
    return f'{self.model} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'guitar_id': self.id})

class Servicing(models.Model):
  date = models.DateField('Servicing Date')
  service = models.CharField(
    max_length=100,
    choices=SERVICE,
    default=SERVICE[0][0]
  )

  guitar = models.ForeignKey(
    Guitar,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f'{self.get_service_display()} on {self.date}'

  class Meta:
    ordering = ['-date']