from django.shortcuts import render
from .forms import UserDetailForm
from .models import UserDetail

def form_view(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            user_detail = UserDetail(
                name=form.cleaned_data['name'],
                father_name=form.cleaned_data['father_name'],
                mother_name=form.cleaned_data['mother_name'],
                education=form.cleaned_data['education'],
                gender=form.cleaned_data['gender'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                marital_status=form.cleaned_data['marital_status'],
                husband_wife_name=form.cleaned_data['husband_wife_name'],
                native=form.cleaned_data['native'],
                current_resident=form.cleaned_data['current_resident'],
                baptism_details=form.cleaned_data['baptism_details'],
                contact_number=form.cleaned_data['contact_number']
            )
            user_detail.save()  # Save the instance to the database
            
            return render(request, 'form/success.html', {'name': form.cleaned_data['name']})
    else:
        form = UserDetailForm()
    
    return render(request, 'form/form.html', {'form': form})