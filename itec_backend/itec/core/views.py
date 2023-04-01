from django.shortcuts import render
from django.http import JsonResponse
from . import api
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def index(request):
    if request.method == 'POST':
        text = request.POST.get('prompt')
        # text = 'Foaie verde, trandafir, am baut azi-noapte vin'
        prompt = "Scrie o poezie care începe cu: \""+text+"\""+""
        poem = api.generate_poem(prompt)
        dic = {'poem':poem}
        return JsonResponse(dic)
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
@api_view(['GET'])
def getData(request):
    person = {'name':'Robert', 'age':29}
    return Response(person)

@csrf_exempt
def apiPost(request):
    if request.method == 'POST':
        text = request.POST.get('promptInput')
        # text = 'Foaie verde, trandafir, am baut azi-noapte vin'
        prompt = "Scrie o poezie care începe cu: \""+text+"\""+""
        poem = api.generate_poem(prompt)
        dic = {'poem':poem}
        return JsonResponse(dic)
    else:
        return JsonResponse({'error': 'Invalid request method'})