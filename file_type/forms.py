from django import forms


class ContentAddressabletForm(forms.Form):
    file_name = forms.CharField()
