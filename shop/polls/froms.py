from django import forms

class User_Form(forms.Form):
    name =  forms.CharField(max_length=50)
    age = forms.IntegerField()
    email = forms.EmailField()