from django import forms


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
