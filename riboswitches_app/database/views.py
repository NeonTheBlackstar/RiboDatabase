from django.shortcuts import render
from django.http import JsonResponse

from django.db.models import CharField
from django.db.models import  Q

from .models import Gene, Organism, Ligand, RiboFamily, Record, RiboClass, Taxonomy, LigandClass
import json

def index(request):

    context = {'breadcrumbs': []}
    return render(request, 'database/index.html', context)

def searcher_ajax(request):

    return render(request, 'database/searcher.html')

def get_records_by_ajax(request):

    l = []
    term = request.GET['term']

    ligands = Ligand.objects.filter(name__icontains=term)

    for e in Record.objects.all():
        if e.family != None:
            for i in ligands:
                if i.name in str(e.family.ribo_class.ligands.all()):
                    l.append(e.name)

    context = {
        'records': l,
    }

    return JsonResponse(context)

def class_family_browser(request):

    result = []
    families = []
    class_list = RiboClass.objects.all()

    for i in RiboClass.objects.all():
        dic = {
            'name': None,
            'families': None,
        }
        dic['name'] = i.name
        for j in RiboFamily.objects.all():
            if j.ribo_class.name == i.name:
                families.append(j.name)
            dic['families'] = families
        families = []
        result.append(dic.copy())

    context = {
        'result': result,
    }

    print(context)

    return render(request, 'database/class_family_browser.html', context)

#########################################################################
########################## TO DO ########################################
def class_family_details(request, family):

    families_list = []

    for e in Record.objects.all():
        if e.family != None:
            if family == e.family.name:
                dic = {
                    'id': e.id,
                    'name': e.name,
                    'gene': None,
                    'organism': None,
                    'ligand': None,
                }
                dic['gene'] = e.gene.name if e.gene != None else dic['gene']
                dic['name'] = e.name if e.name != None else dic['name']
                dic['organism'] = e.gene.organism.scientific_name if e.gene.organism != None else dic['organism']
                dic['ligand'] = e.family.ribo_class.ligands.all()[0].name if e.family.ribo_class.ligands.all() != None else dic['ligand']
                families_list.append(dic.copy())

    context = {
        'families_list': families_list,
    }

    return render(request, 'database/class_family_details.html', context)

def ligand_browser(request):

    ligand_list = Ligand.objects.all()
    context = {
        'ligand_list': ligand_list,
    }

    return render(request, 'database/ligand_browser.html', context)

def ligand_details(request, ligand_name):

    recordList = []
    name = ligand_name

    for e in Record.objects.all():
        if e.family != None:
            if ligand_name in str(e.family.ribo_class.ligands.all()):
                dic = {
                    'id': e.id,
                    # 'gene': None,
                    # 'organism': None,
                    'name': e.name,
                    'ligand': None,
                }
                # dic['gene'] = e.gene.name if e.gene != None else dic['gene']
                # dic['organism'] = e.gene.organism.scientific_name if e.gene.organism != None else dic['organism']
                dic['name'] = e.name if e.name != None else dic['name']
                dic['ligand'] = e.family.ribo_class.ligands.all()[0].name if e.family.ribo_class.ligands.all() != None else dic['ligand']
                recordList.append(dic.copy())

    context = {
        'recordList': recordList,
        'name': name,
    }

    print(recordList)

    return render(request, 'database/ligand_details.html', context)

##########################################################################################

### BEST BROWSER IN THE WHOLE UNIVERSE ###
### KEEP CALM AND BROWSE THE TAXONOMY ###

def create_tax(tax_list, parent_id, data):

    for tax in tax_list:
        tax_name = tax.name
        data.append({
            "id": tax_name, "parent": parent_id, "text": tax_name
        })
        create_tax(
            tax.taxonomy_set.all(), tax_name, data
        )


def organism_browser(request):

    data = []
    counter = 0

    tax_list_tree = []
    current_tax = Taxonomy.objects.get(name = 'Bacteria')
    tax_list_tree.append(current_tax.name)

    data.append({
        "id": current_tax.name, "parent": "#", "text": current_tax.name
    })

    create_tax(current_tax.taxonomy_set.all(), current_tax.name, data)

    d = { 
        'core' : {
            'data' : data,
        },
        'types' : {
            "default" : {
                "icon" : "/static/database/images/folder-24.png"
            },
            "folder-open" : {
                "icon" : "/static/database/images/open-folder-24.png"
            },
        },
        "themes": {
            "dots": True
        },
        "plugins" : [ "types", ] 
    }

    last = []

    for i in range(0, len(d['core']['data'])):
        if d['core']['data'][i]['parent'] != '#':
            try:
                if d['core']['data'][i+1]['parent'] == 'Bacteria':
                    last.append(d['core']['data'][i]['text'])
            except IndexError:
                last.append(d['core']['data'][-1]['text'])

    print(last)

    ddumps = json.dumps(d)

    context = {
        'tax_list_tree': tax_list_tree,
        'd': ddumps,
        'last': last,
    }

    return render(request, 'database/organism_browser.html', context)



##########################################################################################


def organism_details(request, organism_name):

    organism = Organism.objects.filter(scientific_name = organism_name)
    gene = Gene.objects.filter(organism = organism)
    riboswitch_record = Record.objects.filter(gene = gene)
    context = {
        'riboswitch_record': riboswitch_record,
    }

    return render(request, 'database/organism_details.html', context)
