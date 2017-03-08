from django.shortcuts import render

from .models import Gene, Organism, Ligand, RiboFamily, Record, RiboClass


#TODO: urls, collapse, jquery datatables, ajax


def index(request):

	return render(request, 'database/index.html')

def searcher(request):

	return render(request, 'database/searcher.html')

def family_browser(request):

	class_list = RiboClass.objects.all()
	context = {
		'class_list': class_list,
	}

	return render(request, 'database/family_browser.html', context)

def family_detail(request, class_name):

	record_list = []

	for i in RiboFamily.objects.all():
		if class_name in str(i.name):
			dic = {
				'name': None,
			}
			dic['name'] = i.name
			record_list.append(dic.copy())

	context = {
		'record_list': record_list,
	}

	return render(request, 'database/family_detail.html', context)

def ligand_browser(request):

	ligand_list = Ligand.objects.all()
	context = {
		'ligand_list': ligand_list,
	}

	return render(request, 'database/ligand_browser.html', context)

def ligand_detail(request, ligand_name):

	recordList = []

	for e in Record.objects.all():
		if ligand_name in str(e.family.ligands.all()):
			dic = {
				'id': e.id,
				'gene': None,
				'organism': None,
				'ligand': None,
			}
			dic['gene'] = e.gene.name if e.gene != None else dic['gene']
			dic['organism'] = e.gene.organism.scientific_name if e.gene.organism != None else dic['organism']
			dic['ligand'] = e.family.ligands.all()[0].name if e.family.ligands.all() != None else dic['ligand']
			recordList.append(dic.copy())

	context = {
		'recordList': recordList,
	}

	#riboswitch_family = RiboFamily.objects.filter(ligands = riboswitch_ligand)
	#riboswitch_record = Record.objects.filter(family = riboswitch_family)

	return render(request, 'database/ligand_detail.html', context)

def organism_browser(request):

	organism_list = Organism.objects.all()
	context = {
		'organism_list': organism_list,
	}
	
	return render(request, 'database/organism_browser.html', context)

def organism_detail(request, organism_name):

	organism = Organism.objects.filter(scientific_name = organism_name)
	gene = Gene.objects.filter(organism = organism)
	riboswitch_record = Record.objects.filter(gene = gene)
	context = {
		'riboswitch_record': riboswitch_record,
	}

	return render(request, 'database/organism_detail.html', context)