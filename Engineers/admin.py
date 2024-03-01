from django.contrib import admin

# Register your models here.
from Engineers.models import *

admin.site.register(Category)
admin.site.register(Engineer)
admin.site.register(Engineerproject)
admin.site.register(ProjectImage)
admin.site.register(Review)
admin.site.register(Wishlist)