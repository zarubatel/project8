from xml.dom.minidom import Element
from django.shortcuts import render
from .models import Order
from . forms import OrderForm

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', { 'object_list': object_list, 'form' : form })

def thanks(request):
    name1 = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name1, order_phone = phone)
    element.save()
    return render(request, './thanks.html', { 'name' : name1, 'phone' : phone })