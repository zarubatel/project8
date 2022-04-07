from xml.dom.minidom import Element
from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CMS_SLIDER
from price.models import  PriceCard, PriceTable

# Create your views here.
def first_page(request):
    slider_list  = CMS_SLIDER.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    dict_obj = {'slider_list': slider_list,
                'pc_1':pc_1,
                'pc_2':pc_2,
                'pc_3':pc_3,
                'price_table':price_table,
                } 
    return render(request, './index.html', dict_obj )

def thanks(request):
    name1 = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name1, order_phone = phone)
    element.save()
    return render(request, './thanks.html', { 'name' : name1, 'phone' : phone })