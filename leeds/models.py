from django.db import models
from django_countries.fields import CountryField
from authentication.models import User

class Leed(models.Model):
    class SALUTATION_OPTIONS(models.TextChoices):
        Mr = "Mr","Mr"
        Mrs = "Mrs","Mrs",
        Dr = "Dr","Dr"
        
    class SOURCE_OPTIONS(models.TextChoices):
        direct_visit = "DIRECT VISIT","DIRECT VISIT",
        enquiry = "ENQUIRY","ENQUIRY",
        instagram = "INSTAGRAM","INSTAGRAM"
    
    company_name = models.CharField(max_length=150)
    salutation = models.CharField(max_length=150,choices=SALUTATION_OPTIONS.choices)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150,unique=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    country = CountryField(blank_label="(select country)", null=True, blank=True)
    state = models.CharField(max_length=150,null=True,blank=True)
    city = models.CharField(max_length=150,blank=True,null=True)
    #BUSSINESS DETAILS
    executive = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    source = models.CharField(max_length=150,null=True,choices=SOURCE_OPTIONS.choices)
    designation = models.CharField(max_length=150,null=True)
    product = models.CharField(max_length=150)
    requirement = models.CharField(max_length=250,blank=True,null=True)
    notes = models.CharField(max_length=250,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.company_name
    
    
    