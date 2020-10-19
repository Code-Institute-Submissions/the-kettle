from django.shortcuts import render, redirect 

# Create your views here.


def view_basket(request):
    """ Shopping bag is returned """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('basket', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['basket'] = bag
    print(request.session['basket'])
    return redirect(redirect_url)