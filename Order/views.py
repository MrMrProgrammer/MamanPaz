from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Order, OrderDetail
from Food.models import FoodsModel
from BaseApp.models import User
from Moms.models import MomsModel


def add_to_order(request: HttpRequest):
    food_id = request.GET.get('food_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        food = FoodsModel.objects.filter(id=food_id).first()
        if food is not None:
            current_order: Order = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order = current_order[0]
            current_order_detail = current_order.orderdetail_set.filter(food_id=food_id, is_paid=False).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, food_id=food_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found'
            })


    else:
        return JsonResponse({
            'status': 'not_auth'
        })

    return HttpResponse(f'food id : {food_id} - count : {count}')


def CalculateOrder(request: HttpRequest):
    order_id = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    orderDetail = OrderDetail.objects.filter(order_id=order_id).count()
    print(orderDetail)
    return HttpResponse(orderDetail)


def ShowCart(request: HttpRequest):
    order_id = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    order_details = OrderDetail.objects.filter(order_id=order_id)

    sumCart = 0

    for i in order_details:
        if not i.is_paid:
            item = i.count * i.food.food_price
            sumCart += item

    context = {
        'order_details': order_details,
        'sumCart': sumCart,
    }

    return render(request, 'Order/showCart.html', context)


def removePerOrder(request: HttpRequest, orderDetailId):
    order_id = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    OrderDetail.objects.filter(order_id=order_id, id=orderDetailId).delete()

    return redirect('Show-Cart')


def showMomOrders(request: HttpRequest):
    user_id = request.user.id

    is_mom = User.objects.filter(id=request.user.id, is_mom=True)

    if is_mom:
        mom_id = MomsModel.objects.filter(user_id=request.user.id).first()

        momOrders = OrderDetail.objects.filter(food__mom_id=mom_id.id, is_paid=True)

        context = {
            'momOrders': momOrders,
        }

        return render(request, 'Order/showMomOrders.html', context)
    else:
        return HttpResponseNotFound()


def zarinPal(request):
    order_id = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    order_details = OrderDetail.objects.filter(order_id=order_id)

    sumCart = 0

    for i in order_details:
        if not i.is_paid:
            item = i.count * i.food.food_price
            sumCart += item

    context = {
        'sumCart': sumCart,
    }

    return render(request, 'Order/zarinPal.html', context)


def pay_cart(request):
    order_id = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    order_details: OrderDetail = OrderDetail.objects.filter(order_id=order_id)

    for item in order_details:
        if not item.is_paid:
            totall = item.food.food_price * item.count
            mom: MomsModel = MomsModel.objects.filter(id=item.food.mom.id).first()
            mom.wallet += totall
            mom.save()
            print(totall)

    for i in order_details:
        if not i.is_paid:
            i.is_paid = True
            i.food.food_order += i.count
            i.save()
            i.food.save()

    return redirect('Show-Cart')
