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

    for i in Organism.objects.all():
        names.append(str(i.scientific_name))

    for i in term:
        for j in names:
            if term.lower() in j.lower():
                if not any(d['name'] == j for d in l): # if dict doesn't contains the name
                    l.append({'name':j, 'url':'http://www.google.com'},)

    return JsonResponse(l, safe=False)


def ligands(request):
    term = request.GET['term']
    limit = request.GET['limit']
    names = []
    l = []

    for i in Ligand.objects.all():
        names.append(str(i.name))

    for i in term:
        for j in names:
            if term.lower() in j.lower():
                if not any(d['name'] == j for d in l): # if dict doesn't contains the name
                    l.append({'name':j, 'url':'http://www.google.com'},)

    return JsonResponse(l, safe=False)
