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
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'input border border-gray-300 p-2 rounded-md'
            }),
            'marital_status': forms.RadioSelect(attrs={'class': 'radio'}),
            'husband_wife_name': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Spouse name'}),
            'native': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Your native'}),
            'current_resident': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Current location'}),
            'baptism_details': forms.RadioSelect(attrs={'class': 'radio'}),
            'contact_number': forms.TextInput(attrs={'class': 'input border border-gray-300 p-2 rounded-md', 'placeholder': 'Mobile number'}),
        }

    # Make sure no "null" option is added
    gender = forms.ChoiceField(choices=UserDetail.GENDER_CHOICES, widget=forms.RadioSelect, required=True)
    marital_status = forms.ChoiceField(choices=UserDetail.MARITAL_STATUS_CHOICES, widget=forms.RadioSelect, required=True)
    baptism_details = forms.ChoiceField(choices=UserDetail.BAPTISM_CHOICES, widget=forms.RadioSelect, required=True)
