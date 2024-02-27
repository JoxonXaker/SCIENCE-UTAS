from django.urls import path
from dinamic import views


urlpatterns = [
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('about/update/<int:pk>', views.AboutUpdateView.as_view(), name='aboutedit'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    # path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon')
]