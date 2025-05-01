from django import forms
from .models import UserDetail

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Your full name'}),
            'father_name': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': "Father's name"}),
            'mother_name': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': "Mother's name"}),
            'education': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': "Highest qualification"}),
            'gender': forms.RadioSelect(attrs={'class': 'radio'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'datepicker input border border-gray-300 p-2 rounded-md'}),
            'marital_status': forms.RadioSelect(attrs={'class': 'radio'}),
            'husband_wife_name': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Spouse name'}),
            'native': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Your native'}),
            'current_resident': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Current location'}),
            'baptism_details': forms.RadioSelect(attrs={'class': 'radio'}),
            'contact_number': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Mobile number'}),
        }
        
    # Define required fields
    name = forms.CharField(required=True)
    contact_number = forms.CharField(required=True)
    current_resident = forms.CharField(required=True)
    
    # Make sure no "null" option is added and mark as required
    gender = forms.ChoiceField(choices=UserDetail.GENDER_CHOICES, widget=forms.RadioSelect, required=True)
    baptism_details = forms.ChoiceField(choices=UserDetail.BAPTISM_CHOICES, widget=forms.RadioSelect, required=True)
    
    # Non-required fields
    marital_status = forms.ChoiceField(choices=UserDetail.MARITAL_STATUS_CHOICES, widget=forms.RadioSelect, required=True)
    father_name = forms.CharField(required=False)
    mother_name = forms.CharField(required=False)
    education = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=True)
    native = forms.CharField(required=False)
    husband_wife_name = forms.CharField(required=False)

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',
            'admin/js/admin_datepicker.js',
        )
        css = {
            'all': ('https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',)
        }
