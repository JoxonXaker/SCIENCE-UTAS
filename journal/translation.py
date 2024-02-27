from modeltranslation.translator import TranslationOptions, register
from journal import models


@register(models.JournalModel)
class JournalModelTranslationOptions(TranslationOptions):
    fields = ('title','detail', 'lead_editor', 'director', )

# @register(models.ArticleModel)
# class ArticleModelTranslationOptions(TranslationOptions):
#     fields = ()

@register(models.OrganizationModel)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('name', 'detail', 'address')


