from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = Product.objects.get(id = request.POST["id"]).price
    total_charge = quantity_from_form * price_from_form
    request.session['id'] = request.POST["id"]
    
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    
    return redirect( "/checkout/success")

def success(request):

    user_total=0
    for item in Order.objects.all():
        user_total+= item.total_price

    content = {
        'desc': Product.objects.get(id = request.session['id']).description,
        'order': Order.objects.last(),
        'qty': Order.objects.last().quantity_ordered,
        'total': Order.objects.last().total_price,
        'total_orders': Order.objects.last().id,
        'total_user': user_total
    }
    return render(request,'store/checkout.html',content)