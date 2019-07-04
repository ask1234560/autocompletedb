from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from .models import Company
from django.db.models import Q
import json

# Create your views here.

res=[]

def home(request):
    form=forms.Search()
    return render(request,'home.html',{"form":form})

def search(request,s):
    print("in search",s)
    try:
        q=Company.objects.filter( Q(name__istartswith=s) | Q(sym__istartswith=s ) )
        for i in q:
            s=s.upper()
            name=i.name.capitalize()
            sym=i.sym.capitalize()
            if( name.startswith(s) ):
                res.append(name)
            if( sym.startswith(s) ):
                res.append(sym)
        print(res)

    except Exception as e:
        print("Error",e)

    return HttpResponse(json.dumps({"res":res}),content_type="application/json")


