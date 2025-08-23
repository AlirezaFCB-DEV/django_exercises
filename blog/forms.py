from django import forms


class Add_Post(forms.Form):
    title = forms.CharField(required=True , label="Title", max_length=50)
    post_url = forms.SlugField(label="PostUrl")
    content = forms.Textarea(label="Content")
    