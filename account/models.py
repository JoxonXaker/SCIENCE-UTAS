from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class CustomUser(AbstractUser):
    bio = models.CharField(_('bio'), max_length=512, null=True, blank=True)
    address = models.CharField(_('address'), max_length=512, null=True, blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatar', null=True, blank=True)
    # contact
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    # social media    
    facebook = models.CharField(_('facebook'), max_length=64, null=True, blank=True)
    telegram = models.CharField(_('telegram'), max_length=64, null=True, blank=True)
    instagram = models.CharField(_('instagram'), max_length=64, null=True, blank=True)
    whatsapp = models.CharField(_('whatsapp'), max_length=64, null=True, blank=True)


    def imageURL(self):
        if self.avatar:
            return self.avatar.url
        return 'https://secure.gravatar.com/avatar/fa30bc8456490156b8c74c33e5163016?s=32&d=mm&r=g'
    
    def __str__(self) -> str:
        return super().__str__()