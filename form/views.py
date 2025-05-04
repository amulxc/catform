from django.shortcuts import render, redirect
from .forms import UserDetailForm

def user_form(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form-success')
    else:
        form = UserDetailForm()
    return render(request, 'form/user_form.html', {'form': form})

def form_success(request):
    return render(request, 'form/success.html')

def index(request):
    return render(request, 'form/index.html')
