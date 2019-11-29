from django.db import models

# Create your models here.
# class donor(models.Model):
class AvailableCity(models.Model):
    city_name=models.CharField(max_length=100,null=False)

class AvailableBloodGroups(models.Model):
    blood_group=models.CharField(max_length=10,null=False)

class NeedBlood(models.Model):
    blood_group=models.CharField(max_length=10,null=False)
    city = models.CharField(max_length=100,null=False)
    requestname = models.CharField(max_length=100,null=False)
    contact = models.CharField(max_length=10,null=False)


class DonateBlood(models.Model):
    blood_group=models.CharField(max_length=10,null=False)
    city = models.CharField(max_length=100,null=False)
    donorname = models.CharField(max_length=100,null=False)
    contact = models.CharField(max_length=10,null=False)

class Blood_Bank(models.Model):
    blood_bank_name = models.CharField(max_length=120,null=False)
    A_plus = models.IntegerField()
    A_minus = models.IntegerField()
    AB_plus = models.IntegerField()
    AB_minus = models.IntegerField()
    B_plus = models.IntegerField()
    B_minus = models.IntegerField()
    O_plus = models.IntegerField()
    O_minus = models.IntegerField()
    contact_no = models.IntegerField()
    address = models.CharField(max_length=100,null=False)
    adress_key = models.TextField(default="India")

class Blood_Camps(models.Model):
    blood_camp_name = models.CharField(max_length=120,null=False)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=100,null=False)
    adress_key = models.TextField(default="India")

class fact(models.Model):
    factt= models.TextField()

class chart(models.Model):
    height=models.CharField(max_length=100,null=False)
    man=models.CharField(max_length=100,null=False)
    woman=models.CharField(max_length=100,null=False)