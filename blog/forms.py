from django import forms
from .models import Profile


class Add_Post(forms.Form):
    title = forms.CharField(required=True, label="Title", max_length=50)
    post_url = forms.SlugField(
        required=False, label="PostUrl", allow_unicode=True)
    content = forms.CharField(widget=forms.Textarea, label="Content")

    #! custom validation
    def clean_title(self):
        data = self.cleaned_data["title"]
        if "@" in data:
            raise forms.ValidationError("the title is not supported @ ")
        return data

    def clean(self):
        cleaned_data = super().clean()
        post_url = cleaned_data.get("post_url")
        title = cleaned_data.get("title")
        if post_url == title:
            raise forms.ValidationError("post url incorrect")
        return post_url, title

class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email"]

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        if "@" in data:
            raise forms.ValidationError("first name is not valid!!")
        return data

