from django.shortcuts import render
from .models import Item
from django.http import JsonResponse 
# Create your views here.

def items(request,id):
    if request.method == 'GET':
        data = Item.objects.filter(id=id).values()
        return JsonResponse(data,safe = False)

def purchase(request,id):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        quantity = request.POST['quantity']

        item = Item.objects.filter(id=item_id)
        item.quantity = item.quantity - quantity
        item.save()
        return JsonResponse({result:'Purchased'})