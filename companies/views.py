from django.shortcuts import render, redirect
from .models import *
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .sheet import form_responses, process_response

# Create your views here.
#class Profileview(viewsets.ModelViewSet):
    #queryset= Profile.objects.all()
    #serializer_class = ProfileSerializer
def homepage(request):
    '''
    assuming we make the api call hapa
    
    '''
    # form_data=form_responses()
    form_data=form_responses()

    return render(request,'index.html',{'data':form_data})
    