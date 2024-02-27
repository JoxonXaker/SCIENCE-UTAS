from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from ckeditor.fields import RichTextField

from journal.models import JournalModel

class ArticleModel(models.Model):
    STATUS = (
        ('waiting', _('Waiting')),
        ('confirmed', _('Confirmed')),
        ('reediting', _('Reediting')),
        ('canceled', _('Canceled')),
    )
    
    # author
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    
    # by journal
    journal = models.ForeignKey(JournalModel, on_delete=models.CASCADE, null=True, blank=True)
    
    # status 
    status = models.CharField(_('status'), choices=STATUS, max_length=10, default='waiting')
    
    
    # about article
    title = models.CharField(_('title'), max_length=256, null=True, blank=True)
    about = models.CharField(_('about'), max_length=512, null=True, blank=True)
    files = models.FileField(_('files'), upload_to="article/files", null=True, blank=True)
    detail = RichTextField(_('detail'), null=True, blank=True)
    
    # some information
    created = models.DateField(_('created'), auto_now_add=True)
    updated = models.DateField(_('updated'), auto_now=True)
    
    # contact
    phone = models.CharField(_('phone_number'), max_length=64, null=True, blank=True)
    email = models.EmailField(_('email'), max_length=64, null=True, blank=True)
    
    # social media
    video = models.CharField(_('video'), max_length=256, null=True, blank=True)
    facebook = models.CharField(_('facebook'), max_length=64, null=True, blank=True)
    telegram = models.CharField(_('telegram'), max_length=64, null=True, blank=True)
    instagram = models.CharField(_('instagram'), max_length=64, null=True, blank=True)
    youtube = models.CharField(_('youtube'), max_length=64, null=True, blank=True)
    website = models.CharField(_('website'), max_length=64, null=True, blank=True)
    whatsapp = models.CharField(_('whatsapp'), max_length=64, null=True, blank=True)
    
    # is_read 
    is_read_by_admin = models.BooleanField(default=False)
    is_view_by_owner = models.BooleanField(default=False)

    
    class Meta:
        ordering = ['-id']
        
    def fileURL(self):
        if self.files:
            return self.files.url
        return ''

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])


class DeadlineModel(models.Model):
    name = models.CharField(_('deadline name'), max_length=64, null=True)
    about = RichTextField(_('about'), null=True)
    date = models.DateField(_('date'), null=True)
    
    
    
class CommentModel(models.Model):
    created_at = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    comment = models.CharField(_('comment'), max_length=255, null=True, blank=True)
    created = models.DateField(_('created'), auto_now_add=True)
    is_read = models.BooleanField(default=False)


