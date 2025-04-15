from django.db import models

class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    date_of_birth = models.DateField()

    MARITAL_STATUS_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    marital_status = models.CharField(max_length=3, choices=MARITAL_STATUS_CHOICES)

    husband_wife_name = models.CharField(max_length=100, blank=True)
    native = models.CharField(max_length=100)
    current_resident = models.CharField(max_length=100, blank=True)

    BAPTISM_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    baptism_details = models.CharField(max_length=3, default='No')

    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name
