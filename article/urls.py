from django.urls import path
from article import views

urlpatterns = [
    path('', views.ArticleModelListView.as_view(), name='articles'),
    path('profile', views.ProfileArticleModelView.as_view(), name='articles_profile'),
    path('create', views.ArticleCreateView.as_view(), name='article_create'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>', views.ArticleUpdateView.as_view(), name='article_delete'),
    path('<int:id>', views.ArticleDetailView.as_view(), name='article_detail'),
]