from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import mixins
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import date

from article import models, forms

class ArticleModelListView(generic.ListView):
    model = models.ArticleModel
    context_object_name = 'objects'
    template_name = 'article/index.html'
    
    def get(self, request, *args, **kwargs):
        filter: str = self.request.GET.get('filter')
        if filter in ['my', 'mycheck', 'myignore', 'myreview']:
            if self.request.user.is_anonymous:
                return redirect('login')
            
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        return self.render_to_response(context)
    
    def get_queryset(self) -> QuerySet[Any]:
        filter: str = self.request.GET.get('filter')
        
        
        if filter == 'my':
            return super().get_queryset().filter(author=self.request.user)
        elif filter == 'mycheck':
            return super().get_queryset().filter(author=self.request.user)
        elif filter == 'myignore':
            return super().get_queryset().filter(author=self.request.user)
        elif filter == 'myreview':
            return {}
        return super().get_queryset().filter()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # @TODO make popular articles by likes and views
        kwargs['popular_articles'] = self.model.objects.filter()[:5]
        return super().get_context_data(**kwargs)
    
   
class ArticleDetailView(generic.DetailView):
    model = models.ArticleModel
    context_object_name = 'object'
    template_name = "article/detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(models.ArticleModel, id=self.kwargs.get('id'))
        
    def get_context_data(self, **kwargs):
        kwargs['author'] = self.get_object().author
        return super().get_context_data(**kwargs)
       
    
class ProfileArticleModelView(SuccessMessageMixin, mixins.LoginRequiredMixin, generic.ListView):
    model = models.ArticleModel
    context_object_name = 'objects'
    template_name = 'account/article/articles_list.html'
    

    def get_queryset(self) -> QuerySet[Any]:
        filter: str = self.request.GET.get('filter')
        search: str = self.request.GET.get('search')
        delete: str = self.request.GET.get('delete')
        query = super().get_queryset()
        
        if delete:
            if delete.isdigit():
                if query.filter(id=delete):
                    query.filter(id=delete).delete()
                    return query
        
        if filter == 'check':
            query = query.filter(author=self.request.user)
        elif filter == 'ignore':
            query = query.filter(author=self.request.user)
        elif filter == 'review':
            query = {}
        else: query = query.filter(author=self.request.user)
        
        if search:
            query = query.filter(Q(title=search)|Q(about=search)|Q(detail=search))
            
        return query

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        return super().get_context_data(**kwargs)
   

class ArticleUpdateView(SuccessMessageMixin, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    model = models.ArticleModel
    form_class = forms.ArticleForms  
    template_name = "account/article/article_update.html"
    
    def get_success_url(self) -> str:
        return self.request.path
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        messages.success(self.request, _("Your article is changed successfully!"))
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm):
        messages.error(self.request, _("You made a mistake somewhere, please check again!"))
        return super().form_invalid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
# 
class ArticleCreateView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.CreateView):
    model = models.ArticleModel
    form_class = forms.ArticleForms
    success_url = reverse_lazy('articles_profile')
    template_name = "account/article/article_create.html"
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any):
        pk = self.request.GET.get('journal')
        if pk:
            if pk.isdigit():
                query = models.JournalModel.objects.filter(id=pk)
                if query:
                    if query[0].is_deadline:
                        return super().get(request, *args, **kwargs)         
        return redirect('coming_soon')  
    

    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        pk = self.request.GET.get('journal')
        if pk:
            if pk.isdigit():
                query = models.JournalModel.objects.filter(id=pk)
                if query:
                    if query[0].is_deadline:
                        return super().post(request, *args, **kwargs)
        return redirect('coming_soon')  
    
    # bu objectni oladi classni ichida malumotlar bn ishlash uchun
    def get_object(self, queryset=None):
        return super().get_object(queryset)
    
    # bu yangi templatega objectlar uzatadi
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    # 
    def form_valid(self, form):
        messages.success(self.request,  _("Your Article is create successfully!"))
        form.instance.author = self.request.user 
        form.instance.journal = models.JournalModel.objects.filter(id=self.request.GET.get('journal'))[0]
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm):
        messages.error(self.request, _("You made a mistake somewhere, please check again!"))
        return super().form_invalid(form)

    # bu userni tekshiradi 
    def test_func(self):
        return self.request.user.is_authenticated   
 
 
class ArticleDeleteView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.DeleteView):
    model = models.ArticleModel
    success_url = reverse_lazy('articles_profile')

    def test_func(self):
        return self.get_object().author == self.request.user
    
    def delete(self, request: HttpRequest, *args: str, **kwargs: Any):
        title = self.get_object().title
        messages.success(self.request,  _(f"Your`s article is delete successfully!"))
        return super().delete(request, *args, **kwargs)

    
class MessagesModelListView(SuccessMessageMixin, mixins.LoginRequiredMixin, generic.ListView):
    model = models.ArticleModel
    context_object_name = 'objects'
    template_name = 'account/articles_list.html'
    

    def get_queryset(self) -> QuerySet[Any]:
        filter: str = self.request.GET.get('filter')
        search: str = self.request.GET.get('search')
        delete: str = self.request.GET.get('delete')
        query = super().get_queryset()
        
        if delete:
            if delete.isdigit():
                if query.filter(id=delete):
                    query.filter(id=delete).delete()
                    return query
        
        if filter == 'check':
            query = query.filter(author=self.request.user)
        elif filter == 'ignore':
            query = query.filter(author=self.request.user)
        elif filter == 'review':
            query = {}
        else: query = query.filter(author=self.request.user)
        
        if search:
            query = query.filter(Q(title=search)|Q(about=search)|Q(detail=search))
            
        return query

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
   

class MessageModelDetailView(generic.DetailView):
    model = models.ArticleModel
    context_object_name = 'object'
    template_name = "article/detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(models.ArticleModel, id=self.kwargs.get('id'))
        
    def get_context_data(self, **kwargs):
        kwargs['author'] = self.get_object().author
        return super().get_context_data(**kwargs)
    


