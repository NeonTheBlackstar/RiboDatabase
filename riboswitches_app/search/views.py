from django.shortcuts import render
from django.http import JsonResponse

from database.models import Organism, Ligand


def index(request):
    context = {'breadcrumbs': []}
    return render(request, 'search/index.html', context)


def riboswitches(request):
    term = request.GET['term']
    limit = request.GET['limit']
    names = []
    l = []

    for o in Organism.objects.filter(scientific_name__contains=term):
        l.append({'name':o.scientific_name, 'url':'http://www.google.com'},)

    return JsonResponse(l, safe=False)


def ligands(request):
    term = request.GET['term']
    limit = request.GET['limit']
    names = []
    lig = []

    for l in Ligand.objects.filter(name__contains=term):
        lig.append({'name':o.scientific_name, 'url':'http://www.google.com'},)

    return JsonResponse(l, safe=False)
