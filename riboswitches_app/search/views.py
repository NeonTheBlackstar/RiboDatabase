from django.shortcuts import render
from django.http import JsonResponse

from collections import OrderedDict

from database.models import Record, Ligand, Gene, Organism, Aptamer, Article


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
    terminator_width = 0
    promoter_width = 0
    shinedalgarno_width = 0
    aptamer_width = 0
    aug_width = 0
    riboswitch_start = 0
    riboswitch_end = 0

    # Początek ryboprzełącznika to start promotora lub start aptameru, gdy go nie ma
    # Pozycja startu genu, to pozycja startu AUG, za ktorym dodajemy jeszcze 20nt
    # Sprawdzic te aptamery, ktore sa wczytywane przez nas

    # Odrzucamy z nazwy dwie pierwsze litery "RS", a część liczbową konwertujemy do Integera
    for r in Record.objects.filter(id=int(riboswitch_name[2:])):
        context['Name'] = r.name()
        context['Organism'] = r.gene.organism.scientific_name
        context['Class'] = r.family.ribo_class.name
        context['Family'] = r.family.name
        lig = r.family.ribo_class.ligands.all()

        if not lig.exists():
            context['Ligand'] = 'None'
        else:
            lig_list = [str(l) for l in list(lig)]
            context['Ligand'] = ', '.join(lig_list)
            
        context['Gene'] = r.gene.name
        context['Promoter'] = r.promoter
        context['Aptamer position'] = r.aptamer_set.all()[0]
        context['Shine-Dalgarno'] = r.shinedalgarno
        context['Terminator'] = r.terminator
        context['Mechanism'] = r.get_mechanism_display()
        context['Effect'] = r.get_effect_display()
        context['Sequence'] = r.sequence
        articles = r.articles.all()

        if r.promoter != None:
            sequence_length = (r.gene.position.start + 20) - r.promoter.start
        else:
            sequence_length = (r.gene.position.start + 20) - r.aptamer_set.all()[0].position.start


        if r.shinedalgarno != None:
            shinedalgarno_length = r.shinedalgarno.end - r.shinedalgarno.start
            shinedalgarno_width = (shinedalgarno_length/sequence_length) * 100
            shinedalgarno_left = (r.shinedalgarno.start * 100)/sequence_length

        # Start of a riboswitch is equal to start of a promoter or an aptamer, if promoter doesn't exists
        if r.promoter != None:
            promoter_length = r.promoter.end - r.promoter.start
            promoter_width = (promoter_length/sequence_length)*100
            promoter_left = (r.promoter.start * 100)/sequence_length
            riboswitch_start = r.promoter.start
        else:
            riboswitch_start = r.aptamer_set.all()[0].position.start
            promoter_left = 0

        aptamer_length = r.aptamer_set.all()[0].position.end - r.aptamer_set.all()[0].position.start
        aptamer_width = (aptamer_length * 100) / sequence_length
        aptamer_left = (r.aptamer_set.all()[0].position.start - riboswitch_start) * 100 / sequence_length

        # End of a riboswitch is equal to start of a gene or end of a terminator
        riboswitch_end = r.gene.position.start + 20
        if r.terminator != None:
            #st, en = sorted([r.terminator.start, r.terminator.end])
            terminator_length = r.terminator.end - r.terminator.start
            terminator_width = (terminator_length * 100) / sequence_length
            terminator_left = (r.terminator.start - riboswitch_start) * 100 /sequence_length

            if r.terminator.end > riboswitch_end:
                riboswitch_end = r.terminator.end

        if r.gene.position.start != None:
            aug_start = r.gene.position.start
            aug_width = 3
            aug_left = (aug_start - riboswitch_start) * 100 /sequence_length
        else:
            aug_start = 0
            aug_width = 0
            aug_left = 0

    if not articles.exists():
        context['Articles (Pubmed ID)'] = 'No articles found'
    else:
        newlist = [str(t) for t in list(articles)]
        context['Articles (Pubmed ID)'] = ', '.join(newlist)


    l.append(context)
    test = {
        'l': l,
        'name': context['Name'],
        'terminator_width': terminator_width,
        'terminator_left': terminator_left,
        'promoter_width': promoter_width,
        'promoter_left': promoter_left,
        'aptamer_width': aptamer_width,
        'aptamer_left': aptamer_left,
        'aug_width': aug_width,
        'aug_left': aug_left,
        'znak': 'A',
    }

    return render(request, 'search/record.html', test)