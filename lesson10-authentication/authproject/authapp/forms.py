from django import forms
from django.contrib.auth.models import User #This is what we shall use to let the user see enter the app.

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(min_length=10,widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=10,widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']
        
    def clean(self):
        cleaned_data = super().clean() #This impliments all the constraints provided.
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        #Checks if the passwords match 
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!!")
        return cleaned_data
