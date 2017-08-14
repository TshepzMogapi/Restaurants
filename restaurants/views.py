from django.shortcuts import render, get_object_or_404
from . models import Location

def index(request):
	all_locations = Location.objects.all().order_by('location_name')
	context = {'all_locations' : all_locations}
	return render(request,'restaurants/index.html',context)

def detail(request,location_id):
	#try:
	#	location = Location.objects.get(pk=location_id)
	#except Location.DoesNotExist:
	#	raise Http404("Location is not in our Databse yet.")
	location = get_object_or_404(Location,pk=location_id)
	return render(request,'restaurants/detail.html',{'location':location})

