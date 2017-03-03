from django.shortcuts import render

from .models import Gene, Organism, Ligand, RiboFamily, Record

def index(request):

	return render(request, 'database/index.html')

def searcher(request):

	return render(request, 'database/searcher.html')

def ligand_browser(request):

	ligand_list = Ligand.objects.all()
	context = {
		'ligand_list': ligand_list,
	}

	return render(request, 'database/ligand_browser.html', context)

def ligand_detail(request, ligand_name):

	riboswitch_ligand = Ligand.objects.filter(name = ligand_name)
	riboswitch_family = RiboFamily.objects.filter(ligands = riboswitch_ligand)
	riboswitch_record = Record.objects.filter(family = riboswitch_family)
	context = {
		'riboswitch_ligand': riboswitch_ligand,
		'riboswitch_record': riboswitch_record,
	}

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