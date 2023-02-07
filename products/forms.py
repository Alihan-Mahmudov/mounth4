from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=1, max_length=500)

