from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class District(models.Model):
    district = models.CharField(max_length=255, unique=True)
    wiki_link = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.district


class Branch(models.Model):
    branch = models.CharField(max_length=255, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch


class Application(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_no = models.IntegerField()
    email_address = models.EmailField(max_length=30, unique=True)
    address = models.CharField(max_length=30)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    acc_t = (
        ('Savings Account', 'Savings Account'),
        ('Current Account', 'Current Account')
    )
    account_type = models.CharField(max_length=30, choices=acc_t)
    material_provided = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
