from django import forms

from app.models import *

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets={'password':forms.PasswordInput}

class EducationForm(forms.ModelForm):
    class Meta():
        model=Education
        fields=['qualification','address']