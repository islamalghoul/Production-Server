from django.contrib import admin
from .models import CustomUser
# Register your models here.
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_fieldsets=((
        'None',
        {
            'fields':('username','email','password1','password2')
        }
    ),(
        'personal Information',{
            'fields':('first_name','last_name','phone')
        }
    )
    )


admin.site.register(CustomUser,CustomUserAdmin)