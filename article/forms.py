from django import forms
from article import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class ArticleForms(forms.ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('title'), 'class': 'input-text'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('about'), 'style': 'height: 100px; max-height: 150px;'}))
    files = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'uploadButton-input'}),
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])]
    )
    # detail = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('detail'), 'class': 'input-text'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('phone'), 'class': 'input-text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': _('email'), 'class': 'input-text'}))
    facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('facebook'), 'class': 'input-text'}), label='<t style="color: #3b5998;"><i class="fa fa-facebook-square"></i> Facebook</t>')
    telegram = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('telegram'), 'class': 'input-text'}), label='<t style="color: #1da1f2;"><i class="fa fa-telegram"></i> Telegram</t>')
    instagram = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('instagram'), 'class': 'input-text'}), label='<t style="color: #e1306c;"><i class="fa fa-instagram"></i> Instagram</t>')
    youtube = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('youtube'), 'class': 'input-text'}), label='<t style="color: #e31837;"><i class="fa fa-youtube-square"></i> YouTube</t>')
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('website'), 'class': 'input-text'}), label='<t style="color: #52c35a;"><i class="fa fa-internet-explorer"></i> WebSite</t>')
    whatsapp = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('whatsapp'), 'class': 'input-text'}), label='<t style="color: #00a884;"><i class="fa fa-whatsapp"></i> WebSite</t>')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # HELP TEXT
        self.fields['title'].help_text = _("title")
        self.fields['files'].help_text = _("files")
        self.fields['about'].help_text = _("about")
        self.fields['detail'].help_text = _("detail")
        
        self.fields['phone'].help_text = _("phone")
        self.fields['email'].help_text = _("email")
        self.fields['video'].help_text = _("The video must belong to Youtube")
        self.fields['facebook'].help_text = _("facebook")
        self.fields['telegram'].help_text = _("telegram")
        self.fields['instagram'].help_text = _("instagram")
        self.fields['youtube'].help_text = _("youtube")
        self.fields['website'].help_text = _("website")
        self.fields['whatsapp'].help_text = _("whatsapp")

        
    class Meta: 
        model = models.ArticleModel
        fields = (
            'title', 'files',
            'about', 'detail', 
            
            'phone', 'email',
            'video', 'website',
            'facebook','telegram',
            'instagram','youtube',
            'whatsapp'
        )
        # exclude = (
        #     'phone', 'email',
        #     'video', 'website',
        #     'facebook','telegram',
        #     'instagram','youtube',
        #     'whatsapp'
        # )
        
        