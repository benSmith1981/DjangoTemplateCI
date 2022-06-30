from django import forms
from .models import Item

# Create your models here.
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']