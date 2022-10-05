from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Products

# Create your views here.


class InventoryView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            inventary = list(Products.objects.filter(id=id).values())
            if len(inventary) > 0:
                product = inventary[0]
                datos = {'message': 'Success', 'inventory': product}
            else:
                datos = {'message': 'Inventory not found ...'}
            return JsonResponse(datos)
        else:
            inventary = list(Products.objects.values())
            if len(inventary) > 0:
                datos = {'message': 'Success', 'inventory': inventary}
            else:
                datos = {'message': 'Inventory not found ...'}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Products.objects.create(name=jd['name'], type=jd['type'], description=jd['description'],
                                stock=jd['stock'], bodega_id_id=jd['bodega_id_id'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        inventary = list(Products.objects.filter(id=id).values())
        if len(inventary) > 0:
            product = Products.objects.get(id=id)
            product.name = jd['name']
            product.type = jd['type']
            product.description = jd['description']
            product.stock = jd['stock']
            product.save()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Inventory not found ...'}
        return JsonResponse(datos)

    def delete(self, request):
        pass
