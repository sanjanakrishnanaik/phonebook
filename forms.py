from django import forms
from .models import Contact, Category

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
