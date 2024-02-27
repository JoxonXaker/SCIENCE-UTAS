from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': _('Enter your password')}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': _('Confirm your password')}),
    )
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)        
        
        self.fields['email'].help_text = 'Your email address will not be displayed publically'
        self.fields['password1'].help_text = [
                'Your password can’t be too similar to your other personal information.',
                'Your password must contain at least 8 characters.',
                'Your password can’t be a commonly used password.',
                'Your password can’t be entirely numeric.'   
            ]
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': _('Username')}),
            'email': forms.TextInput(attrs={'placeholder': _('Email address')}),
        }


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('username'), 'class': 'input-text'}), min_length=2)
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('first_name'), 'class': 'input-text'}), min_length=2,)
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('last_name'), 'class': 'input-text'}), min_length=2,)

    # avatar = forms.ImageField(
    #     required=False, 
    #     widget=forms.FileInput(attrs={'class': 'uploadButton-input'}),
    #     # validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', ])]
    # )
    address = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'placeholder': _('address'), 'style': 'height: 100px; max-height: 150px;'}),
        min_length=5,
        )
    bio = forms.CharField(
        required=False, 
        widget=CKEditorWidget(),
        min_length=5,
        # validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', ])]
    )
    # contact
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('phone'), 'class': 'input-text'}), min_length=7)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': _('email'), 'class': 'input-text'}), min_length=7)
    # social media
    facebook = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': _('facebook'), 'class': 'input-text'}), label='<t style="color: #3b5998;"><i class="fa fa-facebook-square"></i> Facebook</t>',
        min_length=5,    
    )
    telegram = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': _('telegram'), 'class': 'input-text'}), label='<t style="color: #1da1f2;"><i class="fa fa-telegram"></i> Telegram</t>',
        min_length=5,    
    )
    instagram = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': _('instagram'), 'class': 'input-text'}), label='<t style="color: #e1306c;"><i class="fa fa-instagram"></i> Instagram</t>',
        min_length=5,    
    )
    whatsapp = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': _('whatsapp'), 'class': 'input-text'}), label='<t style="color: #5fc964;"><i class="fa fa-whatsapp"></i> Whatsapp</t>',
        min_length=5,    
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'username', 'avatar',
            'first_name','last_name',
            
            'email','phone_number', 
            'bio',  'address',
            
            'facebook','whatsapp',
            'telegram','instagram',    
            
            # 'password', 'password1', 'password2'
        )
    
    
class CustomPasswordChangeForm(PasswordChangeForm):
    
    class Meta: 
        model = CustomUser
        