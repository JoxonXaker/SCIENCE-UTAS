from django import forms
from modeltranslation.forms import TranslationModelForm


from dinamic import models


class AboutModelForm(TranslationModelForm, forms.ModelForm):
    class Meta:
        model = models.AboutModel
        fields = ('title', 'detail')
        
