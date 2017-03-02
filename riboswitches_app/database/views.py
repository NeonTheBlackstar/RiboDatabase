from django.shortcuts import render

from .models import Ligand

def index(request):

	return render(request, 'database/index.html')

def browser(request):

	ligand_list = Ligand.objects.all()
	context = {
		'ligand_list': ligand_list,
	}

	return render(request, 'database/browser.html', context)

def detail(request, name):

	l = Ligand.objects.get()