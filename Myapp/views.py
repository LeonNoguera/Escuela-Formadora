from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from Myapp.models import Colchon, Estudiante
# Create your views here.

def home(requers):
    resid=Estudiante.objects.all()
    return render(requers,'home.html',{
        'estudiantes':resid
    })


def res_1(requers):
    resid=Estudiante.objects.all()
    

    return render(requers,'resi_1.html',{
        'estudiantes':resid
        
    })

def res_2(requers):
    resists=Estudiante.objects.all()
    
    return render(requers,'resi_2.html',{
        'estudiantes': resists
    })


def res_3(requers):
    resists=Estudiante.objects.all()
    return render(requers,'resi_3.html',{
        'estudiantes': resists
    })

def res_4(requers):
    resists=Estudiante.objects.all()
    return render(requers,'resi_4.html',{
        'estudiantes': resists
    })


def res_5(requers):
    resists=Estudiante.objects.all()
    return render(requers,'resi_5.html',{
        'estudiantes': resists
    })


def res_6(requers):
    resists=Estudiante.objects.all()
    return render(requers,'resi_6.html',{
        'estudiantes': resists
    })