from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
 
from .models import User, Role
 
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
    


 
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message')
    list_filter = ('content_type','action_flag')
    search_fields = ['user__username',]
    date_hierarchy = 'action_time'

    
admin.site.register(LogEntry, LogEntryAdmin)