from django.shortcuts import render
from django.http import JsonResponse

from .models import Gene, Organism, Ligand, RiboFamily, Record, RiboClass, Taxonomy, \
                    LigandClass
import json, re

def help(request):

    return render(request, 'database/help.html')

def contact(request):

    context = {
        'api_key': 'AIzaSyAVR8tS7DwduYSSWCkKgAgjKuS1ZGyWaeA',
    }

    return render(request, 'database/contact.html', context)

def index(request):

    context = {'breadcrumbs': []}
    return render(request, 'database/index.html', context)

def searcher(request):

    recordList = []

    for e in Record.objects.all():
        if e.family != None:
            dic = {
                'name': e.name,
                'ligand': None,
                'organism': None,
            }
            dic['ligand'] = e.family.ribo_class.ligands.all()[0].name if e.family.ribo_class.ligands.all() else dic['ligand']
            dic['organism'] = e.gene.organism.scientific_name if e.gene.organism.scientific_name != None else dic['organism']
            recordList.append(dic.copy())

    context = {
        'recordList': recordList,
    }

    return render(request, 'database/searcher.html', context)

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
            print(j)
            if j.ribo_class.name == i.name:
                families.append(j.name)
            dic['families'] = families
        families = []
        result.append(dic.copy())
    context = {
        'result': result,
    }
    print(context['result'])

    return render(request, 'database/class_family_browser.html', context)

def class_family_details(request, family):

    families_list = []

    for e in Record.objects.all():
        if e.family != None:
            if family == e.family.name:
                organism = e.gene.organism.scientific_name
                families_list.append(organism)

    context = {
        'families_list': set(families_list),
    }

    return render(request, 'database/class_family_details.html', context)

def gene_details(request, gene_name):

    recordList = []
    name = gene_name

    for e in Record.objects.all():
        if gene_name in str(e.gene.name):
            dic = {
                'id': e.id,
                'name': e.name(),
                'gene': None,
            }
            dic['name'] = e.name() if e.name() != None else dic['name']
            dic['gene'] = e.gene.name if e.gene.name != None else dic['gene']
            recordList.append(dic.copy())

    context = {
        'recordList': recordList,
        'name': name,
    }

    return render(request, 'database/ ils.html', context)


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
                    'name': e.name,
                    'ligand': None,
                }
                dic['name'] = e.name if e.name != None else dic['name']
                dic['ligand'] = e.family.ribo_class.ligands.all()[0].name if e.family.ribo_class.ligands.all() != None else dic['ligand']
                recordList.append(dic.copy())

    context = {
        'recordList': recordList,
        'name': name,
    }

    return render(request, 'database/ligand_details.html', context)

### BEST BROWSER IN THE WHOLE UNIVERSE ###

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

    parents = []
    childrens = []

    for i in data:
        parents.append(i['parent'])

    for i in data:
        if i['id'] not in parents:
            childrens.append(i['id'])

    ddumps = json.dumps(d)

    context = {
        'tax_list_tree': tax_list_tree,
        'd': ddumps,
        'childrens': childrens,
    }

    return render(request, 'database/organism_browser.html', context)



##########################################################################################


def organism_details(request, organism_name):

    term = request.get_full_path()
    match = re.findall(r'[/](.*?)[/]',term)[-1].replace('%20', ' ')

    print(match)

    riboswitch_record = []

    for e in Record.objects.all():
        if match == str(e.gene.organism.scientific_name):
            dic = {
                'id': e.id,
                'name': e.name(),
                'scientific_name': None,
            }
            dic['name'] = e.name() if e.name() != None else dic['name']
            dic['scientific_name'] = e.gene.organism.scientific_name if e.gene.organism.scientific_name != None else dic['scientific_name']
            riboswitch_record.append(dic.copy())

    context = {
        'riboswitch_record': riboswitch_record,
    }

    print(context)

    return render(request, 'database/organism_details.html', context)
