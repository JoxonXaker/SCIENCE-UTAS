from django import forms as df
from modeltranslation import forms as mf, widgets 
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin
from journal import models


# class ArticleModelForm(mf.TranslationModelForm):
#     class Meta:
#         model = models.ArticleModel
#         fields = ['title']
#         languages = ["uz", "ru", "en"]
#         fallback_language = "uz"
#         widgets = {
#             'title': mf.forms.URLInput,
            # 'title_ru': widgets.Widget(), 
            # 'title_en': widgets.Widget(),
        # }
        
        # fields = ['title','valume','published','image','files','detail','director','lead_editor','editors','experts']

# class ArticleModelForm(mf.TranslationModelForm):
#     class Meta:
#         model = models.ArticleModel
#         fields = ['title', 'title_uz', 'title_ru', 'title_en', 'valume']
#         # ['title','valume','published','image','files','detail','director','lead_editor','editors','experts']
#         # widgets = {
#         #     'field1': forms.TextInput(attrs={'class': 'custom-class'}),
#         #     'field2': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
#         #     # Add more fields and their corresponding widgets as needed
#         # } 
#         exclude = []      