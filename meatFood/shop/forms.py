from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CartForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30, required=False)
    phone_number = PhoneNumberField(region="US")
    user_address = forms.CharField(max_length=150)
    comment = forms.CharField(max_length=500, required=False)
    slugs_quantity = forms.CharField(required=False)
    
