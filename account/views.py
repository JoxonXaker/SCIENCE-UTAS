from django.forms import BaseModelForm
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django import http
from django.shortcuts import redirect


from account.models import CustomUser
from account import forms


class SignUpView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
class ProfilePasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    model = CustomUser
    success_url = reverse_lazy('password_change')
    success_message = _('Your password is changed successfully!')
    template_name = 'account/password_change.html'

    
class ProfileEditView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    # model = CustomUser
    form_class = forms.CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'account/profile.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        messages.success(self.request, _("Your profile is changed successfully!"))
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm):
        messages.error(self.request, _("You made a mistake somewhere, please check again!"))
        return super().form_invalid(form)
    
    def get_object(self, queryset=None):
        return self.request.user