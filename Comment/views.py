from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from .models import Comment, Answer


def add_comment_answer(request: HttpRequest):
    print(request.user.is_mom)

    comment_id = request.GET.get('comment_id')
    answer_text = request.GET.get('answer_text')

    com: Comment = Comment.objects.filter(id=comment_id).first()
    food_id = com.food_id

    print(f'comment id : {comment_id} - answer text : {answer_text}')

    new_answer = Answer(
        answer_text=answer_text,
        comment_id=comment_id,
    )
    new_answer.save()

    current_comment = Comment.objects.filter(id=comment_id).first()
    current_comment.is_answered = True

    current_comment.save()

    print(food_id)

    return redirect('FoodDetails', food_id=food_id)

# food_id = request.GET.get('food_id')
# count = request.GET.get('count')
#
# if request.user.is_authenticated:
#     food = FoodsModel.objects.filter(id=food_id).first()
#     if food is not None:
#         current_order: Order = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
#         current_order = current_order[0]
#         current_order_detail = current_order.orderdetail_set.filter(food_id=food_id, is_paid=False).first()
#         if current_order_detail is not None:
#             current_order_detail.count += int(count)
#             current_order_detail.save()
#         else:
#             new_detail = OrderDetail(order_id=current_order.id, food_id=food_id, count=count)
#             new_detail.save()
#
#         return JsonResponse({
#             'status': 'success'
#         })
#     else:
#         return JsonResponse({
#             'status': 'not_found'
#         })
#
#
# else:
#     return JsonResponse({
#         'status': 'not_auth'
#     })
