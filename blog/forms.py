from django import forms


class Add_Post(forms.Form):
    title = forms.CharField(required=True, label="Title", max_length=50 , widget=forms.TextInput(attrs={"class" : "form_title"}))
    post_url = forms.SlugField(
        required=False, label="PostUrl", allow_unicode=True)
    content = forms.CharField(widget=forms.Textarea(attrs={"rows" : 5 , "placeholder" : "Enter Text"}), label="Content")

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

