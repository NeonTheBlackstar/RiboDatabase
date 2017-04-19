from django.shortcuts import render

from .models import Gene, Organism, Ligand, RiboFamily, Record, RiboClass, Taxonomy, LigandClass
import json


#TODO: jquery datatables, ajax


def index(request):

    return render(request, 'database/index.html')

def searcher(request):

    return render(request, 'database/searcher.html')

def class_family_detail(request):

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

    return render(request, 'database/class-family_detail.html', context)

def ligand_browser(request):

    ligand_list = Ligand.objects.all()
    context = {
        'ligand_list': ligand_list,
    }

    return render(request, 'database/ligand_browser.html', context)

def ligand_detail(request, ligand_name):

    recordList = []

    for e in Record.objects.all():
        if e.family != None:
            if ligand_name in str(e.family.ribo_class.ligands.all()):
                dic = {
                    'id': e.id,
                    'gene': None,
                    'organism': None,
                    'ligand': None,
                }
                dic['gene'] = e.gene.name if e.gene != None else dic['gene']
                dic['organism'] = e.gene.organism.scientific_name if e.gene.organism != None else dic['organism']
                dic['ligand'] = e.family.ribo_class.ligands.all()[0].name if e.family.ribo_class.ligands.all() != None else dic['ligand']
                recordList.append(dic.copy())

    context = {
        'recordList': recordList,
    }

    return render(request, 'database/ligand_detail.html', context)

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
        "plugins" : [ "types" ] 
    }

    ddumps = json.dumps(d)

    context = {
        'tax_list_tree': tax_list_tree,
        'd': ddumps,
    }

    return render(request, 'database/organism_browser.html', context)



##########################################################################################


def organism_detail(request, organism_name):

    organism = Organism.objects.filter(scientific_name = organism_name)
    gene = Gene.objects.filter(organism = organism)
    riboswitch_record = Record.objects.filter(gene = gene)
    context = {
        'riboswitch_record': riboswitch_record,
    }

    return render(request, 'database/organism_detail.html', context)
