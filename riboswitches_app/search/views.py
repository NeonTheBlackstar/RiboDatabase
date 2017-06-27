from django.shortcuts import render
from django.http import JsonResponse

from collections import OrderedDict

from database.models import Record, Ligand, Gene, Organism


def index(request):
    context = {'breadcrumbs': []}
    return render(request, 'search/index.html', context)


def genes(request):
    term = request.GET['term']
    limit = request.GET['limit']
    l = []

    for g in Gene.objects.filter(name__icontains=term):
        print(g)
        l.append({'name':g.name, 'url':"/search/gene/{}".format(g.name)},)

    return JsonResponse(l, safe=False)


def organisms(request):
    term = request.GET['term']
    limit = request.GET['limit']
    l = []

    for o in Organism.objects.filter(scientific_name__icontains=term):
        l.append({'name':o.scientific_name, 'url':"/search/organism/{}".format(o.scientific_name.replace(' ', '_'))},)

    return JsonResponse(l, safe=False)


def ligands(request):
    term = request.GET['term'] # ligand name
    limit = request.GET['limit']
    lig = []

    for l in Ligand.objects.filter(name__icontains=term):
        lig.append({'name':l.name, 'url':"/browser/ligand/{}/".format(l.name)},)
    
    return JsonResponse(lig, safe=False)


def record(request, riboswitch_name):
    l = []
    context = OrderedDict()

    # Odrzucamy z nazwy dwie pierwsze litery "RS", a część liczbową konwertujemy do Integera
    for r in Record.objects.filter(id=int(riboswitch_name[2:])):
        context['name'] = r.name()
        context['organism'] = r.gene.organism.scientific_name
        context['family'] = r.family.name
        context['gene'] = r.gene.name
        context['terminator'] = r.terminator
        context['promoter'] = r.promoter
        context['mechanism'] = r.mechanism
        context['effect'] = r.effect
        context['sequence'] = r.sequence

    l.append(context)
    test = {
        'l': l,
        'name': context['name'],
    }

    print(context)

    return render(request, 'search/record.html', test)