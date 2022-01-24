from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model= Login
        fields = '__all__'

# class LoginForm(forms.Form):

#     # label
#     # initial
#     # disabled
#     # help_text
#     # widget
#     # required
    

#     username = forms.CharField(max_length=50, disabled=False, required=True)
#     password = forms.CharField(max_length=50,widget=forms.PasswordInput)