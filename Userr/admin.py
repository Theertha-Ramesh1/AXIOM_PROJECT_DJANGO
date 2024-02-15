from django.contrib import admin

# Register your models here.
from Userr.models import *

admin.site.register(User)
admin.site.register(ImageUser)