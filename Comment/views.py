from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect

from .models import Comment, Answer


def add_comment_answer(request: HttpRequest):
    if request.user.is_authenticated:
        if request.user.is_mom:

            comment_id = request.GET.get('comment_id')
            answer_text = request.GET.get('answer_text')

            new_answer = Answer(
                answer_text=answer_text,
                comment_id=comment_id,
            )
            new_answer.save()

            current_comment = Comment.objects.filter(id=comment_id).first()
            current_comment.is_answered = True

            current_comment.save()

            return JsonResponse({
                'status': 'success',
            })

        else:
            return JsonResponse({
                'status': 'not_permissions'
            })

    else:
        return JsonResponse({
            'status': 'not_permissions'
        })
