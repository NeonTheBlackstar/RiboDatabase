from django.shortcuts import render
from django.http import JsonResponse

from database.models import *


def index(request):
    context = {'breadcrumbs': []}
    return render(request, 'search/index.html', context)


def riboswitches(request):
    term = request.GET['term']
    limit = request.GET['limit']
    print('riboswitches', term, limit)

    l = [
      {'name':term, 'url':'http://www.google.com'},
    ]
    return JsonResponse(l, safe=False)


def ligands(request):
    term = request.GET['term']
    limit = request.GET['limit']
    print('ligands', term, limit)
    l = [
      {'name':'ligand1', 'url':'http://www.google.com'},
      {'name':'ligand2', 'url':'http://www.google.com'},
      {'name':'ligand3', 'url':'http://www.google.com'},
    ]
    return JsonResponse(l, safe=False)
