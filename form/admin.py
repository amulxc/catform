from django.contrib import admin
from .models import UserDetail
from .forms import UserDetailForm
@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    form = UserDetailForm
    list_display = ['name', 'gender', 'marital_status', 'education', 'contact_number']
    search_fields = ['name', 'father_name', 'mother_name', 'native', 'contact_number']
    list_filter = ['gender', 'marital_status', 'education']
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['husband_wife_name'].label = 'Husband / Wife Name'
        return form