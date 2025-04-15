from django.contrib import admin
from .models import UserDetail

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'marital_status', 'education', 'contact_number']
    search_fields = ['name', 'father_name', 'mother_name', 'native', 'contact_number']
    list_filter = ['gender', 'marital_status', 'education']
