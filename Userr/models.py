from django.db import models


# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=30, null=True)
    Mobile = models.CharField(max_length=30, null=True)
    Email = models.CharField(max_length=30, null=True)
    Password = models.CharField(max_length=30, null=True)
    Status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "User"


class ImageUser(models.Model):
    image_id = models.AutoField(primary_key=True)
    user_image = models.ImageField(upload_to="imagess/")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "image_user"




