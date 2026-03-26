from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from application.models import Appointment, Contact, Profile, PaymentMethod
from django import forms




class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'gender', 'date', 'email', 'message']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Gender'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rate': forms.DateInput(attrs={'class ': 'form-control', 'type': 'rate'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write problem/ Issue'}),
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type something'}),
        }

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with your route name
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['payment_method', 'card_number', 'expiry_date', 'cvv', 'bank_name', 'account_number', 'paypal_email']
