from modeltranslation.translator import TranslationOptions, register
from dinamic import models


@register(models.AboutModel)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'detail' )


# @register(models.ContactModel)
# class OrganizationTranslationOptions(TranslationOptions):
#     fields = ('contact_title', 'contact_detail' )



