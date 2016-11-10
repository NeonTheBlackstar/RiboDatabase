from django.http import HttpResponse
from django.template import loader

from .models import Record


def index(request):
	template = loader.get_template('database/index.html')
	return HttpResponse(template.render(request))


def searcher(request):
 
	recordList = []
	
	for e in Record.objects.order_by('id'):
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

	template = loader.get_template('database/searcher.html')
	return HttpResponse(template.render(context, request))