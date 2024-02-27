from typing import Any
from django.contrib.auth import mixins
from django.db.models.query import QuerySet
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from journal import models
from article import models as article
from datetime import datetime



class JournalView(generic.ListView):
    model = models.JournalModel
    context_object_name = 'objects'
    template_name = 'journal/index.html'
    
    def get_object(self, queryset=None):
        return models.JournalModel.objects.all()
    
    def get_context_data(self, **kwargs):
        kwargs['popular_journals'] = self.get_object().filter(is_staf=True)[:3]
        return super().get_context_data(**kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get('filter')=='self':
            return super().get_queryset().filter(is_staf=True).filter(author=self.request.user.id)
        return super().get_queryset().filter(is_staf=True)
   

class JournalDetailView(generic.DetailView):
    model = models.JournalModel
    context_object_name = 'object'
    template_name = "journal/detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(models.JournalModel, slug=self.kwargs.get('slug'))
    
    def get_article_author(self, queryset=None):
        return get_object_or_404(article.ArticleModel, id=self.kwargs.get('id'))
        
    def get_context_data(self, **kwargs):
        kwargs['articles'] = article.ArticleModel.objects.filter(status='confirmed')
        kwargs['organs'] = self.get_object().organ
        return super().get_context_data(**kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class ComingSoonView(generic.ListView):
    model = models.JournalModel
    context_object_name = 'objects'
    template_name = 'other/coming-soon.html'
    
    
    def get_queryset(self) -> QuerySet[Any]:
        query = super().get_queryset()
        current_time = datetime.now()
        return query.filter(deadline__gt=current_time)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for obj in context['objects']:
            obj.formatted_date = obj.deadline.strftime('%Y/%m/%d')
        return context