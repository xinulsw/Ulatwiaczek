# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def test_dodaj(request):
    return HttpResponse("<h1>Dodawanie testu</h1>")

def test_lista(request):
    return HttpResponse("<h1>Lista testów</h1>")

def sprawdzian_dodaj(request):
    return HttpResponse("<h1>Dodawanie sprawdzianu</h1>")

def sprawdzian_lista(request):
    return HttpResponse("<h1>Lista sprawdzianów</h1>")
