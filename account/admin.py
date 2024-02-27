from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.forms import CustomUserChangeForm, CustomUserCreationForm
from account.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','username','first_name','last_name','phone_number','is_staff']
    list_display_links = ['email','username','first_name','last_name','phone_number','is_staff']
    
    normaluser_fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'avatar', 'bio', 'address']
    superuser_fields = ['is_staff', 'is_active']

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = self.normaluser_fields + self.superuser_fields
        else:
            self.fields = self.normaluser_fields

        return super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user)


