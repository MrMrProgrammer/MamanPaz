from django.urls import path
from . import views

urlpatterns = [
    path('momsRegister', views.MomsRegisterView.as_view(), name='MomsRegisterView'),
    path('UpdateMomProfile', views.MomUpdateProfileView.as_view(), name='UpdateMomProfile'),
    path('momsList', views.MomsListView.as_view(), name='momsList'),
    path('profile/<int:mom_id>', views.MomProfile, name='MomProfile'),
    path('foods/', views.FoodListView.as_view(), name='FoodListView'),
    path('foods/<int:food_id>', views.FoodDetails, name='FoodDetails'),
    path('getMomImage/<int:mom_id>', views.getMomProfile, name='getMomImage'),
    path('PerMomFoodsList', views.PerMomFoodsList, name='PerMomFoodsList'),
    path('addFood', views.addFoodView.as_view(), name='addFood'),

]
