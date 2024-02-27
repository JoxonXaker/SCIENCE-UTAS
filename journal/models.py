from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import date
import random
import re

def slugify(text):
    text = text.lower()
    
    text += f' {random.randint(1000, 10000)}'
    
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    
    return text


# @TODO ADD IS_STAFF FIELDS 
class JournalModel(models.Model):
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    organ = models.ForeignKey(to='journal.OrganizationModel', on_delete=models.SET_NULL, null=True, related_name="organization", default=None)
    # #
    title = models.CharField(_('title'), max_length=500, null=True)
    valume = models.CharField(_('valume'), max_length=55, null=True)
    detail = RichTextField(_('detail'), null=True, blank=True)
    # #
    files = models.FileField(_('files'), upload_to="journal/files", null=True, blank=True)
    image = models.ImageField(_('image'), upload_to="journal/photos", null=True, blank=True)
    # #
    director = models.CharField(_('director'), max_length=200, null=True, blank=True)
    lead_editor = models.CharField(_('lead_editor'), max_length=200, null=True, blank=True)
    # #
    published = models.DateField(_('published'), null=True, blank=True)
    created = models.DateField(_('created'), auto_now_add=True)
    updated = models.DateField(_('updated'), auto_now=True)
    deadline = models.DateField(_('deadline'), null=True)
    # #
    slug = models.CharField(_('slug'), max_length=55, null=True, blank=True, default='slug-problem')
    is_staf = models.BooleanField(_('is_staf'), default=False)
    
    # # # # # #
    class Meta:
        ordering = ['-id']
    # # # # # #
    @property
    def is_deadline(self):
        return self.deadline > date.today()
    # # # # # #  
    def imageURL(self):
        if self.image:
            return self.image.url
        return '/static/web/wp-content/uploads/woocommerce-placeholder-300x300.png'
    # # # # # #
    def fileURL(self):
        if self.files:
            return self.files.url
        return ''
    
    # # # # # # 
    def save(self, *args, **kwargs):
        title = 'this journal is currently untitled '
        if(self.title):
            title = str(self.title)
        if(len(title)>50):
            title = title[0:49]
        self.slug = slugify(title)
        super(JournalModel, self).save(*args, **kwargs)
        
    # # # # # # 
    def get_absolute_url(self):
        return reverse('postdetail', args=[self.slug])
    
    def __str__(self):
        return self.title + '. ' + self.valume
    

class OrganizationModel(models.Model):
    image = models.ImageField(_('image'), upload_to='', null=True, blank=True)
    name = models.CharField(_('name'), max_length=255, null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=20, null=True, blank=True)
    email = models.EmailField(_('email'), null=True, blank=True)
    address = models.CharField(_('address'), max_length=500, blank=True, null=True)
    detail = RichTextField(_('detail'), blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('journal_list')
    
    def imageURL(self):
        if self.image:
            return self.image.url
        return '/static/web/wp-content/uploads/woocommerce-placeholder-300x300.png'
    

# class JournalViewsModel(models.Model):
#     created_at = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
#     journal = models.ForeignKey(JournalModel, on_delete=models.CASCADE)


# class JournalDownloadsModel(models.Model):
#     created_at = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
#     journal = models.ForeignKey(JournalModel, on_delete=models.CASCADE)


# class JournalBookmarkModel(models.Model):
#     created_at = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
#     journal = models.ForeignKey(JournalModel, on_delete=models.CASCADE)

    
# class JournalRatingModel(models.Model):
#     RATING_CHOICES = [
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#     ]
#     created_at = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
#     journal = models.ForeignKey(JournalModel, on_delete=models.CASCADE)
    
#     rating = models.IntegerField(_('rating'), choices=RATING_CHOICES, default=0)
#     comment = models.CharField(_('comment'), max_length=255, null=True, blank=True)
#     created = models.DateField(_('created'), auto_now_add=True)

    
# class JournalCommentModel(models.Model):
#     created_at = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
#     journal = models.ForeignKey(JournalModel, on_delete=models.CASCADE)
    
#     comment = models.CharField(_('comment'), max_length=255, null=True, blank=True)
#     created = models.DateField(_('created'), auto_now_add=True)
