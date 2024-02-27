from django.urls import path
from journal import views

urlpatterns = [
    path('journals/', views.JournalView.as_view(), name='journals'),
    # path('create', views.ArticleCreateView.as_view(), name='postcreate'),
    # path('update/<str:slug>', views.ArticleUpdateView.as_view(), name='postedit'),
    path('journals/<str:slug>', views.JournalDetailView.as_view(), name='journals_detail'),
    path('coming-soon', views.ComingSoonView.as_view(), name='coming_soon'),

]


