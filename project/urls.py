from django.contrib import admin
from django.urls import path, include
from django.conf import settings, urls
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views
from django import shortcuts
from project import views

from django.utils.translation import gettext_lazy as _

urls.handler404 = 'project.views.custom_404'

def redirect_to_login(request):
    return shortcuts.redirect(to='admin_login')
 

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/login/', redirect_to_login, name='redirect_to_login'), 
]


urlpatterns += i18n_patterns(
    path('', views.HomePageView.as_view(), name='home'),
    path('', include('dinamic.urls')),
    path('', include('journal.urls')),
    path('articles/', include('article.urls')),

    path('accounts/', include('account.urls')), 
    path('accounts/', include('django.contrib.auth.urls')), 
    # path('admin/login/', views.LoginView.as_view(), name='admin_login'), 
    path('admin/', admin.site.urls, name='admin'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('404/', views.custom_404, name='404')
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ADMIN TITLE CHANGES

admin.site.site_header = _("SCIENCE-UTAS Control Panel")
admin.site.site_title = _("SCIENCE-UTAS | Control Panel")
admin.site.index_title = _("SCIENCE-UTAS | Control Panel")