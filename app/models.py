from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name=models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name


class Branch(models.Model):
    bank_name=models.ForeignKey(Bank,on_delete=models.CASCADE)
    ifsc=models.CharField(max_length=20,primary_key=True)
    branch=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    contact=models.IntegerField()
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=30)

    def __str__(self):
        return self.branch




