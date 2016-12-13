from django.db import models

# Create your models here.
class Acount(models.Model):
    name = models.CharField(max_length=16)
    number = models.CharField(max_length=19, help_text='Enter format: XXXX XXXX XXXX XXXX')
    amount = models.DecimalField(decimal_places=2, default=0, max_digits=300)

class Charge(models.Model):
    transaction = models.DecimalField(decimal_places=2, max_digits=300)
    dat = models.DateField()
    account = models.ForeignKey(Acount, related_name='charge')