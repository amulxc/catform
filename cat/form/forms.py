# form/forms.py
from django import forms

class UserDetailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    father_name = forms.CharField(label='Father Name', max_length=100)
    mother_name = forms.CharField(label='Mother Name', max_length=100)
    education = forms.CharField(label='Education', max_length=100)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)

    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    
    MARITAL_STATUS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    marital_status = forms.ChoiceField(label='Marital Status', choices=MARITAL_STATUS_CHOICES, widget=forms.RadioSelect)
    
    husband_wife_name = forms.CharField(label='Husband/Wife Name', max_length=100, required=False)
    
    native = forms.CharField(label='Native', max_length=100)
    current_resident = forms.CharField(label='Current Resident', max_length=100, required=False)
    
    BAPTISM_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    baptism_details = forms.ChoiceField(label='Baptism Details', choices=BAPTISM_CHOICES, widget=forms.RadioSelect)
    
    contact_number = forms.CharField(label='Contact Number', max_length=15, required=False)