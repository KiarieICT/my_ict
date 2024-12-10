from django import forms


class lets_connect(forms.Form):
    name=forms.CharField(max_length=100,label="Your name")
    email=forms.EmailField(required=True,max_length=250)
    information=forms.Textarea()

