from django.contrib.admin import register
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from dinamic import models


# class OrganizationTabularInline(TranslationStackedInline):
#     model = models.OrganizationModel
    

@register(models.AboutModel)
class AboutModelAdmin(TabbedTranslationAdmin):
#     inlines = [OrganizationTabularInline,]
    list_display = ('title', 'description', 'url')
    list_display_links = ('title', 'description', 'url')

