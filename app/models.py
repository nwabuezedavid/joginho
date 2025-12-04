from django.db import models
import uuid
# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from django.utils import timezone
from .genUid import *


TRANSACTION_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
    ('reversed', 'Reversed'),
    ('cancelled', 'Cancelled'),
]

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Link to Django's user authentication system
    uuid = models.CharField(max_length=40,  blank=True, null=True)
    country = models.CharField(max_length=40,  blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255,  blank=True, null=True)
    city = models.CharField(max_length=100,  blank=True, null=True)
    state = models.CharField(max_length=100,  blank=True, null=True)
    phone = models.CharField(max_length=15,  blank=True, null=True)
    date_of_birth = models.CharField(max_length=40 ,blank=True, null=True)
    gender = models.CharField(max_length=40 ,blank=True, null=True)
    accountnum = models.CharField(max_length=40 ,blank=True, null=True)
    zipcode = models.CharField(max_length=40 ,blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=40,blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    account_type = models.CharField(max_length=40, blank=True, null=True)
    preferred_currency = models.CharField(max_length=40,blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=12, default=0, decimal_places=2)
    deposite = models.ManyToManyField("depositex", blank=True)
    intertransfer = models.ManyToManyField("intertransferx", blank=True)
    localtransfer = models.ManyToManyField("localtransferx", blank=True)
    benfit = models.ManyToManyField("benfitx", blank=True)
    loan = models.ManyToManyField("loanx", blank=True)
    appoved = models.BooleanField(default=False)
    disable = models.BooleanField(default=False)
    swiftcode = models.CharField( max_length=50 ,blank=True, null=True,)
    
    def __str__(self):  
        return f'client {str(self.username)}'
    
    

    

class  benfitx(models.Model):
    uuid = models.CharField( max_length=50 ,blank=True, null=True,)
    accname = models.CharField( max_length=50 ,blank=True, null=True,)
    accnum = models.CharField( max_length=50 ,blank=True, null=True,)
    bankname = models.CharField( max_length=50 ,blank=True, null=True,)
    email = models.CharField( max_length=50 ,blank=True, null=True,)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True,)
    phone = models.CharField( max_length=50 ,blank=True, null=True,)
    swiftcode = models.CharField( max_length=50 ,blank=True, null=True,)
    appoved = models.CharField(blank=True, choices=TRANSACTION_STATUS_CHOICES, null=True,max_length=50)
    class Meta:
        ordering = ['date'] 
    def __str__(self):
        return f'client {str(self.uuid)}'
class  depositex(models.Model):
    uuid = models.CharField( max_length=50 ,blank=True, null=True,)
    Amount = models.CharField( max_length=50 ,blank=True, null=True,)
    method = models.CharField( max_length=50 )
    appoved = models.CharField(max_length=50 )
    date = models.DateTimeField( blank=True,default=timezone.now, null=True,)

    class Meta:
        ordering = ['date'] 
    def __str__(self):
        return f'client {str(self.uuid)}'

class  intertransferx(models.Model):
    uuid = models.CharField( max_length=50 ,blank=True, null=True,default=referCode(12))
    accname = models.CharField( max_length=50 ,blank=True, null=True,)
    accnum = models.CharField( max_length=50 ,blank=True, null=True,default=acc())
    bankname = models.CharField( max_length=50 ,blank=True, null=True,)
    swiftcode = models.CharField( max_length=50 ,blank=True, null=True,default=generate_swift_code())
    ibannumber = models.CharField( max_length=50 ,blank=True, null=True,)
    ountry = models.CharField( max_length=50 ,blank=True, null=True,)
    Amount = models.CharField( max_length=50 ,blank=True, null=True,)
    Description = models.CharField( max_length=900 ,blank=True, null=True,)
    appoved = models.CharField(blank=True, choices=TRANSACTION_STATUS_CHOICES, null=True,max_length=50)

    date = models.DateTimeField( blank=True,default=timezone.now, null=True,)
    class Meta:
        ordering = ['date']  
    def save(self, *args, **kwargs):
        # Generate a new UUID if it doesn't exist
        if not self.uuid:
            new_uuid = str(referCode(9))  # Generate a new UUID

            # Check for duplicates
            while intertransferx.objects.filter(uuid=new_uuid).exists():
                new_uuid = str(referCode(9))  # Generate a new UUID until it's unique

            self.uuid = new_uuid
        
        super().save(*args, **kwargs)
    def __str__(self):
        return f'client {str(self.uuid)}'
        
class  localtransferx(models.Model):
    uuid = models.CharField( max_length=50 ,blank=True, null=True,default=referCode(9))
    accname = models.CharField( max_length=50 ,blank=True, null=True,)
    accnum = models.CharField( max_length=50 ,blank=True, null=True,default=acc())
    bankname = models.CharField( max_length=50 ,blank=True, null=True,)
    Amount = models.CharField( max_length=50 ,blank=True, null=True,)
    Description = models.CharField( max_length=50 ,blank=True, null=True,)
    appoved = models.CharField(blank=True, choices=TRANSACTION_STATUS_CHOICES, null=True,max_length=50)

    date = models.DateTimeField( blank=True, null=True,default=timezone.now)
    class Meta:
        ordering = ['-date'] 
    def save(self, *args, **kwargs):
        # Generate a new UUID if it doesn't exist
        if not self.uuid:
            new_uuid = str(referCode(9))  # Generate a new UUID

            # Check for duplicates
            while localtransferx.objects.filter(uuid=new_uuid).exists():
                new_uuid = str(referCode(9))  # Generate a new UUID until it's unique

            self.uuid = new_uuid
        
        super().save(*args, **kwargs)
    def __str__(self):
        return f'client {str(self.uuid)}'


class loanx(models.Model):
    uuid = models.CharField( max_length=50 ,blank=True, null=True,)
    Types = models.CharField( max_length=50 ,blank=True, null=True,)
    Amount = models.CharField( max_length=50 ,blank=True, null=True,)
    NetIncome = models.CharField( max_length=50 ,blank=True, null=True,)
    Description = models.CharField( max_length=50 ,blank=True, null=True,)
    appoved = models.CharField(blank=True, choices=TRANSACTION_STATUS_CHOICES, null=True,max_length=50)

    date = models.DateTimeField( blank=True, null=True,default=timezone.now)
    class Meta:
        ordering = ['date'] 
    
    def __str__(self):
        return f'client {str(self.uuid)}'



class siteedit(models.Model):
    name = models.CharField( max_length=50 ,blank=True, null=True,)
    email = models.CharField( max_length=50 ,blank=True, null=True,)
    domain = models.CharField( max_length=50 ,default=name, blank=True, null=True,)
    Address = models.CharField( max_length=50 ,blank=True, null=True,)
    country = models.CharField( max_length=50 ,blank=True, null=True,)
    dis = models.TextField( blank=True, null=True,)
    phone = models.CharField( max_length=50 ,blank=True, null=True,)
    logo = models.TextField( blank=True, null=True,)
    image1 = models.TextField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    

   
    def __str__(self):
        return self.name