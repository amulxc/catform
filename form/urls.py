from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form, name='user-form'),
    path('success/', views.form_success, name='form-success'),
]
