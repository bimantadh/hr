from django.db import models

# Create your models here.
class Pay(models.Model):
    payroll_name = models.CharField(max_length= 50)
    amount = models.CharField(max_length= 15)
    deposited_date= models.DateField()
    payed_to= models.CharField(max_length=50)
    payed_by= models.CharField(max_length= 50)

    def __str__  (self):
        return self.payroll_name
    
    