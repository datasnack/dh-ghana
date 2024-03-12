from django.shortcuts import render
from django.contrib.gis.geos import Point

from shapes.models import Shape
from datalayers.models import Datalayer

# Create your views here.

def study_sites(request):

    context = {
        'shapes': None,
        'datalayers': None,
        'point': None,
    }

    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

    if lat is not None and lng is not None:
        point = Point(float(lng), float(lat))
        shapes = Shape.objects.filter(geometry__contains=point).order_by('type__position')
        context['shapes'] = shapes

        context['point'] = point

        all_layers = Datalayer.objects.all()
        context['datalayers'] = []
        for l in all_layers:
            if l.is_loaded():
                context['datalayers'].append(l)



    return render(request, "study_sites.html", context)
