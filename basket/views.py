from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

# Create your views here.


def view_basket(request):
    """ Shopping basket is returned """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Quantity updated in the basket. """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def delete_from_basket(request, item_id):
    """ Delete items from the basket. """
    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)