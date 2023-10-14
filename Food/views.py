from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .forms import AddFoodForm, UpdateFoodForm
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .models import MomsModel, FoodsModel
from Comment.models import Comment, Answer
from Order.models import Order, OrderDetail
from Comment.forms import CommentForm, AnswerForm


class FoodListView(ListView):
    model = FoodsModel
    queryset = FoodsModel.objects.all()
    template_name = 'Food/FoodsList.html'
    context_object_name = 'foods'
    paginate_by = 6


class FoodDetailsView(View):
    def get(self, request, food_id):

        add_comment_form = CommentForm()
        add_answer_form = AnswerForm()

        food: FoodsModel = FoodsModel.objects.filter(id=food_id).first()
        other_food = FoodsModel.objects.filter(mom_id=food.mom_id).order_by('-id')
        comments = Comment.objects.filter(food_id=food_id).order_by('-id')

        order_id = Order.objects.filter(user_id=request.user.id).first()
        user_orders = OrderDetail.objects.filter(food_id=food_id, is_paid=True)

        if user_orders:
            user_can_comment = True
        else:
            user_can_comment = False

        context = {
            'food': food,
            'other_food': other_food,
            'comments': comments,
            'user_can_comment': user_can_comment,
            'add_comment_form': add_comment_form,
            'add_answer_form': add_answer_form,
        }

        return render(request, 'Food/FoodDetails.html', context)

    def post(self, request, food_id):

        add_comment_form = CommentForm(request.POST)
        add_answer_form = AnswerForm(request.POST)

        if add_comment_form.is_valid():
            text = add_comment_form.cleaned_data.get('text')
            ux = add_comment_form.cleaned_data.get('user_experience').id

            new_comment = Comment(
                text=text,
                UX_id=ux,
                food_id=food_id,
                user_id=request.user.id
            )

            new_comment.save()

            return redirect('FoodDetails', food_id=food_id)


        if add_answer_form.is_valid():
            answer_text = add_answer_form.cleaned_data.get('text')
            comment_id = pass
            # add comment id !!!

            new_answer = Answer(
                answer_text=answer_text,
                comment_id=comment_id
            )

            new_answer.save()

            return redirect('FoodDetails', food_id=food_id)


def PerMomFoodsList(request):
    foodsList: FoodsModel = FoodsModel.objects.filter(mom__user_id=request.user.id).order_by('-id')

    context = {
        "foodsList": foodsList,
    }

    return render(request, 'Food/PerMomFoodsList.html', context)


class addFoodView(View):
    def get(self, request):
        add_food_form = AddFoodForm()
        context = {
            'add_food_form': add_food_form,
        }

        return render(request, 'Food/AddFood.html', context)

    def post(self, request):
        mom_id = MomsModel.objects.filter(user_id=request.user.id).first()

        mom_id = mom_id.id

        if mom_id:
            add_food_form = AddFoodForm(request.POST, request.FILES)

            if add_food_form.is_valid():
                food_name = add_food_form.cleaned_data.get('food_name')
                food_price = add_food_form.cleaned_data.get('food_price')
                food_recipe = add_food_form.cleaned_data.get('food_recipe')
                food_photo = add_food_form.cleaned_data.get('food_photo')
                is_active = add_food_form.cleaned_data.get('is_active')
                # raw_material = add_food_form.cleaned_data.get('raw_material')

                new_food = FoodsModel(
                    mom_id=mom_id,
                    food_name=food_name,
                    food_price=food_price,
                    food_recipe=food_recipe,
                    food_photo=food_photo,
                    is_active=is_active,
                    # raw_material=raw_material,
                )

                new_food.save()

            context = {
                'add_food_form': add_food_form,
            }

            return redirect('PerMomFoodsList')

        else:
            return HttpResponseNotFound()


class UpdateFoodView(View):

    def get(self, request: HttpRequest, food_id):
        if request.user.is_mom:

            current_food: FoodsModel = FoodsModel.objects.filter(id=food_id).first()

            food_photo = current_food.food_photo.url

            edit_form = UpdateFoodForm(instance=current_food)

            context = {
                'edit_form': edit_form,
                'food_id': food_id,
                'food_photo': food_photo,
            }

            return render(request, 'Food/UpdateFood.html', context)

        else:
            return HttpResponse('You are not allowed to access this page !')

    def post(self, request: HttpRequest, food_id):

        current_food: FoodsModel = FoodsModel.objects.filter(id=food_id).first()

        edit_form = UpdateFoodForm(request.POST, request.FILES, instance=current_food)

        if edit_form.is_valid():
            edit_form.save(commit=True)

            return redirect('PerMomFoodsList')

        context = {
            'edit_form': edit_form,
        }

        return render(request, 'Food/UpdateFood.html', context)


def removeFood(request: HttpRequest, food_id):
    FoodsModel.objects.filter(id=food_id).delete()

    return redirect('PerMomFoodsList')
