from django.shortcuts import render
from django.http import JsonResponse

from database.models import Record, Ligand


def index(request):
    context = {'breadcrumbs': []}
    return render(request, 'search/index.html', context)


def riboswitches(request):
    term = request.GET['term']
    limit = request.GET['limit']
    l = []

    for r in Record.objects.filter(name__contains=term):
        l.append({'name':r.name, 'url':"/search/record/{}".format(r.name)},)

    return JsonResponse(l, safe=False)


def ligands(request):
    term = request.GET['term']
    limit = request.GET['limit']
    lig = []

    for l in Ligand.objects.filter(name__contains=term):
        lig.append({'name':l.name, 'url':'http://www.google.com'},)

    return JsonResponse(lig, safe=False)

def record(request):

    return render(request, 'search/record.html')