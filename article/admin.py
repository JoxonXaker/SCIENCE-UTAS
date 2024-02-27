from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.forms import Textarea

from typing import Any
from article import models


@admin.register(models.ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created', 'status')
    list_display_links = ('author', 'title', 'created', 'status')

    
    def get_form(self, request: Any, obj: Any | None = ..., change: bool = ..., **kwargs: Any) -> Any:
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['about'].widget = Textarea(attrs={'class': 'vTextField', 'style': 'height: 100px; min-height: 100px; max-height: 200px'})
        return form
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    

@admin.register(models.DeadlineModel)
class DeadlineModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_display_links = ('name', 'date')


@admin.register(models.CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'article', 'is_read')
    list_display_links = ('created_at', 'article', 'is_read')


