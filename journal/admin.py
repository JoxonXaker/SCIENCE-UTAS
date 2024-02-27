from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from journal import models


# class OrganizationTabularInline(TranslationStackedInline):
#     model = models.OrganizationModel
    

@admin.register(models.JournalModel)
class JournalModelAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
    # inlines = [OrganizationTabularInline,]
    prepopulated_fields = {'slug': ('title',),}
    list_display = ('title', 'created_by', 'deadline', 'is_staf')
    list_display_links = ('created_by', 'title', 'deadline', 'is_staf')
    exclude = ('created_by', 'created', 'updated' 'slud')
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()



@admin.register(models.OrganizationModel)
class JournalModelAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',),}
    list_display = ('name', 'phone', 'email')
    list_display_links = ('name', 'phone', 'email')
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)   

