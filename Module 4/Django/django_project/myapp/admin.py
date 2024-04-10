from django.contrib import admin
from .models import *

# Register your models here.
# below code is used for show your tables in django admin panel
class userdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','email','dob','mobilno']


admin.site.register(userinfo,userdata)