from django import forms


class SignupForm(forms.form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)