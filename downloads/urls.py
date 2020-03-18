from django.urls import path

from . import views

urlpatterns = [
	path('arklis_terrain/', views.arklisTerrain, name='arklisTerrain'),
	path('arklis_nature/', views.arklisNature, name='arklisNature'),
	path('arklis_exporter/', views.arklisExporter, name='arklisExporter'),
]