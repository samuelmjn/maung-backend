from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from maung.models import Member
from maung.serializers import MemberSerializer

# Create your views here.
@csrf_exempt
def find_all_members(request):
    if request.method == 'GET':
        limit = int(request.GET["limit"])
        page = int(request.GET["page"])
        offset = (page - 1) * limit
        if offset < 0:
            offset = 0
        members = Member.objects.all() [offset:offset+limit]
        
        serializer = MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(status=400)

def search_members(request):
    if request.method == 'GET':
        keyword = request.GET["keyword"]
        limit = int(request.GET["limit"])
        page = int(request.GET["page"])
        offset = (page - 1) * limit
        if offset < 0:
            offset = 0
        if keyword:
            members = Member.objects.filter(full_name__icontains=keyword) [offset:offset+limit]

        serializer = MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(status=400)