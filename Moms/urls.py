from django.urls import path
from . import views

urlpatterns = [
    path('momsRegister', views.MomsRegisterView.as_view(), name='MomsRegisterView'),
    path('UpdateMomProfile', views.MomUpdateProfileView.as_view(), name='UpdateMomProfile'),
    path('momsList', views.MomsListView.as_view(), name='momsList'),
    path('profile/<int:mom_id>', views.mom_profile, name='MomProfile'),
    path('getMomImage/<int:mom_id>', views.get_mom_profile, name='getMomImage'),
    path('show_mom_wallet', views.show_mom_wallet, name='show_mom_wallet'),
]
