from django.shortcuts import render
from django.http import Http404


def arklisTerrain(request):
	userActive = request.user.is_authenticated

	if not userActive:
		raise Http404
	else:
		return render(request, 'downloads/arklis_terrain.html')


def arklisNature(request):
	userActive = request.user.is_authenticated

	if not userActive:
		raise Http404
	else:
		return render(request, 'downloads/arklis_nature.html')


def arklisExporter(request):
	userActive = request.user.is_authenticated

	if not userActive:
		raise Http404
	else:
		return render(request, 'downloads/arklis_exporter.html')