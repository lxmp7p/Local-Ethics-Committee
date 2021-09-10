from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
 
from .models import User, Role
 
#admin.site.register(User, UserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователи"""
    
    list_display = ('username', 'last_name', 'first_name','middle_name', 'date_joined', 'last_login')
    search_fields = ("username", "last_name")
    list_filter = ("last_login",)
    fieldsets = (
        (None, {
            "fields": (("username",),)
        }),
        (None, {
            "fields": (("last_name", "first_name", "middle_name"),)
        }),
        (None, {
            "fields": (("role",),)
            
        }),
   
    )
    
    

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    """Роли"""
    list_display = ("name",)
    


    