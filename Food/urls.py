from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.FoodListView.as_view(), name='FoodListView'),
    # path('foods/<int:food_id>', views.FoodDetails, name='FoodDetails'),
    path('foods/<int:food_id>', views.FoodDetailsView.as_view(), name='FoodDetails'),
    path('PerMomFoodsList', views.PerMomFoodsList, name='PerMomFoodsList'),
    path('addFood', views.addFoodView.as_view(), name='addFood'),
    path('UpdateFood/<int:food_id>', views.UpdateFoodView.as_view(), name='UpdateFood'),
    path('RemoveFood<int:food_id>', views.removeFood, name='RemoveFood'),
]
