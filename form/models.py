from django.db import models

class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    date_of_birth = models.DateField(help_text="Select your date of birth", verbose_name="Date of Birth", blank=True, null=True)

    MARITAL_STATUS_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    marital_status = models.CharField(max_length=3, choices=MARITAL_STATUS_CHOICES)

    husband_wife_name = models.CharField(max_length=100, blank=True, verbose_name="Husband/ Wife Name")
    native = models.CharField(max_length=100, blank=True)
    current_resident = models.CharField(max_length=100)

    BAPTISM_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    baptism_details = models.CharField(max_length=3, choices=BAPTISM_CHOICES)

    contact_number = models.CharField(max_length=15)
    
    # New fields for tracking creation and modification times
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified")

    def __str__(self):
        return self.name
