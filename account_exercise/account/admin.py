from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Custom_User
# Register your models here.

@admin.register(Custom_User)
class Custom_User_Admin(UserAdmin) :
    model = Custom_User
    
    fieldsets = UserAdmin.fieldsets + (
        (None , {"fields" : ("phone" , "birth_date")}),
    )
