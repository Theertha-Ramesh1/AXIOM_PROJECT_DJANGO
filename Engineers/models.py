from datetime import datetime

from django.db import models
from Userr.models import User


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Category"


class Engineer(models.Model):
    Name = models.CharField(max_length=20, null=True)
    Email = models.CharField(max_length=20, null=True)
    Phone_number = models.CharField(max_length=20, null=True)
    Qualification = models.CharField(max_length=30, null=True)
    Experience = models.CharField(max_length=20, null=True)
    Image = models.ImageField(null=True, upload_to='imagess')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    Password = models.CharField(max_length=30, null=True)
    Create_at = models.DateTimeField(auto_now_add=True, null=True)
    Status = models.CharField(max_length=20, default="Pending", null=True)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "Engineer"


class Engineerproject(models.Model):
    Project_Title = models.CharField(max_length=80, null=True)
    Project_description = models.CharField(max_length=300, null=True)
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, null=True)
    # image = models.ImageField(null=True)
    Place = models.CharField(max_length=300, null=True)
    Start_Date = models.DateField(auto_created=True)
    End_Date = models.DateField()
    Contact_number = models.CharField(max_length=40, null=True)

    # Work_Status = models.CharField(max_length=20, default="Completed, Ongoing, Upcoming")

    def __str__(self):
        return self.Project_Title

    class Meta:
        db_table = "Engineer_Project"


class ProjectImage(models.Model):
    ProjectImg = models.ImageField(upload_to="imagess/", null=True)
    Project = models.ForeignKey(Engineerproject, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "ProjectImages"


# class PlanType(models.Model):
#     userrr = models.ForeignKey(User,on_delete=models.CASCADE)
#     Type_of_Plan = models.CharField(max_length=200,default="Basic Plan")


class Review(models.Model):
    Review = models.CharField(max_length=300)
    Rating = models.CharField(max_length=20)
    Project = models.ForeignKey(Engineerproject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Review"





class Engineer_contact_enquiryy(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=30, null=True)
    purpose = models.CharField(max_length=200, null=True)
    eng = models.ForeignKey(Engineer,on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = "engineer_contact_enquiry2"


class Wishlist(models.Model):
    project= models.ForeignKey(Engineerproject,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table = "Wishlist"