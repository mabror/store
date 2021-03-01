from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Income, Outgoung,Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'amount')

class RegisterForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        fields = ( 'first_name', 'username', 'password')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['product', 'amount',]
        

class ExpenceForm(forms.ModelForm):
    class Meta:
        model = Outgoung
        fields = ['product', 'amount',]
