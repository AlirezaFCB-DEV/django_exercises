from django import forms


class Add_User(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput, min_length=8)
    email = forms.EmailField(required=True, widget=forms.EmailInput)
