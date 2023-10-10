from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Order, OrderDetail
from Moms.models import FoodsModel


def add_to_order(request: HttpRequest):
    food_id = request.GET.get('food_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        food = FoodsModel.objects.filter(id=food_id).first()
        if food is not None:
            current_order: Order = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order = current_order[0]
            current_order_detail = current_order.orderdetail_set.filter(food_id=food_id).first()
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
