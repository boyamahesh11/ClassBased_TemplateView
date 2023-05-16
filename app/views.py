from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse

class Wbv(TemplateView):
    template_name='cbv.html'
    def get_context_data(self,**kwargs):
        w=WebpageForm()
        co=super().get_context_data(**kwargs)
        co['w']=w
        return co

    def post(self,request):
        wo=WebpageForm(request.POST)
        if wo.is_valid():
            wo.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data is not correct')
            


        
