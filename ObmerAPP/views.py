from django.shortcuts import render
from .models import Images
from django.http import JsonResponse
from django.views import View


def prepareOption(View):
    data = Images.objects.all()
    result = []
    for i in data:
        result.append({'title': i.title, 'url': i.image.url, 'id': i.id, 'size': i.image.size})
    return JsonResponse(result, safe=False)


def home_page(request):
    data = Images.objects.all()
    return render(request, 'home_page.html', {'data': data})
