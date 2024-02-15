from django.db import models
from Engineers.models import *


# Create your models here.
class Admin_UserEnquiry(models.Model):
    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=200)
    Email = models.CharField(max_length=40)
    Phone = models.CharField(max_length=20)
    Location = models.CharField(max_length=30)
    Purpose = models.CharField(max_length=300)

    class Meta:
        db_table = "Admin User Enquiry"