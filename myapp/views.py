from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from .models import  Language
from utils.db import session

def index(request,**kwargs):
    lang = session.query(Language).all()
    data = {'lang': lang}
    return render(request,'index.html',data)
