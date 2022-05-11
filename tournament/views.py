from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tournament.models import Team
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.
@csrf_exempt
def list_team(request):
    print(request.content_params)
    print(dir(request))
    if request.method == 'GET':
        #print(request)
        if "country" in request.GET:
            teams = Team.objects.filter(country=request.GET['country'])
        else:
            teams = Team.objects.all()
        #body = json.loads(request.body.decode('utf-8'))
        #print(body)
        #teams = Team.objects.all()
        #print(teams)
        #return JsonResponse(serializers.serialize('json', teams), safe=False)
        return JsonResponse(serializers.serialize(queryset=teams, format='json'), safe=False)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        #new_team = Team(name=data['name'], description=data['description'], country=data['country'], logo=data['logo'])
        #new_team.save()
        new_team = Team.objects.create(**data)
        return JsonResponse(serializers.serialize(queryset=[new_team], format='json'), safe=False)
        
    if request.method == 'DELETE':
        data = json.loads(request.body)
        #team = Team.objects.get(id=data['id'])
        team = Team.objects.get(pk=data['id'])
        team.delete()
        return HttpResponse(status=204)
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        #team = Team.objects.get(id=data['id'])
        team = Team.objects.get(pk=data['id'])
        team.name = data['name']
        team.save()
        return JsonResponse(serializers.serialize(queryset=[team], format='json'), safe = False)
        
        #return HttpResponse('List team Prueba')
        