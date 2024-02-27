from django.views import generic
from journal import models as journal
from account import models as account
from article import models as article
from django import shortcuts


def custom_404(request, exception=None):
    return shortcuts.render(request, 'other/404.html', status=404)  

class HomePageView(generic.ListView):
    model = journal.JournalModel
    context_object_name = 'objects'
    template_name = 'home.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(is_staf=True)
    
    def get_context_data(self, **kwargs):
        articles = article.ArticleModel.objects.all()
        kwargs['statistic'] = {
            'users': account.CustomUser.objects.all().count(),
            'journals': journal.JournalModel.objects.filter(is_staf=True).count(),
            'article': articles.count(),
            'checked': articles.filter(status='confirmed').count(),
        }
        return super().get_context_data(**kwargs)