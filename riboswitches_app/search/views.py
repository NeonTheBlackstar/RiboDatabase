from django.shortcuts import render
from django.http import JsonResponse

from database.models import Record, Ligand, Gene, Organism


def index(request):
    context = {'breadcrumbs': []}
    return render(request, 'search/index.html', context)


def riboswitches(request):
    term = request.GET['term']
    limit = request.GET['limit']
    l = []

    for r in Record.objects.filter(name__icontains=term):
        l.append({'name':r.name, 'url':"/search/record/{}".format(r.name)},)

    return JsonResponse(l, safe=False)


def ligands(request):
    term = request.GET['term'] # ligand name
    limit = request.GET['limit']
    lig = []

    for l in Ligand.objects.filter(name__contains=term):
        lig.append({'name':l.name, 'url':"/browser/ligand/{}/".format(l.name)},)
    
    return JsonResponse(lig, safe=False)

def record(request, riboswitch_name):
    l = []
    context = {}

    for r in Record.objects.filter(name=riboswitch_name):
        context['name'] = r.name
        context['organism'] = r.gene.organism.scientific_name
        context['family'] = r.family.name
        context['gene'] = r.gene.name
        context['terminator'] = r.terminator
        context['promoter'] = r.promoter
        context['mechanism'] = r.mechanism
        context['effect'] = r.effect

    l.append(context)
    test = {
        'l': l,
        'name': context['name'],
    }

    print(context)

    return render(request, 'search/record.html', test)