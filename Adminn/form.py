from Engineers .models import *
from Userr .models import *
from django import forms

class AdminCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={'placeholder': "Enter Category", 'class': 'form-control', })
        }

class AdmiUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields =  "__all__"