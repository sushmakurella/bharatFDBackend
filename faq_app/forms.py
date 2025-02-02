from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget

class FAQForm(forms.ModelForm):
    question = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter question'})
    )
    answer = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control ckeditor-custom'})
    )

    class Meta:
        model = FAQ
        fields = ['question', 'answer']
