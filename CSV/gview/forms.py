from django import forms

class UploadFileForm(forms.form):
    title = forms.CharField(max_length=100)
    file = forms.FileField 