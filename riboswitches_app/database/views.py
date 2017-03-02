from django.shortcuts import render

from .models import Ligand, RiboFamily, Record

def index(request):

	return render(request, 'database/index.html')

def browser(request):

	ligand_list = Ligand.objects.all()
	context = {
		'ligand_list': ligand_list,
	}

	return render(request, 'database/browser.html', context)

def detail(request, ligand_name):

	riboswitch_ligand = Ligand.objects.get(name = ligand_name)
	context = {
		'riboswitch_ligand': riboswitch_ligand,
	}

	return render(request, 'database/detail.html', context)