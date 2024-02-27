from django.shortcuts import render
from django.views import generic
from dinamic import models, forms
from django.urls import reverse_lazy

#  
class AboutPageView(generic.ListView):
    model = models.AboutModel
    fields = '__all__'
    context_object_name = 'objects'
    template_name = 'about.html'
    
#  
class AboutUpdateView(generic.UpdateView):
    model = models.AboutModel
    fields = '__all__'
    success_url = reverse_lazy('about')
    template_name = 'about_edit.html'
    
class AboutDeleteView(generic.DeleteView):
    model = models.AboutModel
    success_url = reverse_lazy('about')
    template_name = 'about_edit.html'    
        
#  
class ContactPageView(generic.ListView):
    model = models.AboutModel
    fields = '__all__'
    context_object_name = 'objects'
    template_name = 'other/contact.html'
    
#  

class ComingSoonView(generic.TemplateView):
    template_name = 'other/coming-soon.html'