from django.shortcuts import render, HttpResponse
from .models import Store
from .serializer import StoreSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    return render(request,'index.html')

# @api_view(['GET','POST'])
# def store_data(request):
#     st = Store.objects.all()
#     sr = StoreSerializer(st,many=True)
#     # json_data = JSONRenderer().render(sr.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return Response(sr.data)
    # return HttpResponse(str(sr.data))
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer