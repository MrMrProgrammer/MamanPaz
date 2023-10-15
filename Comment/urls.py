from django.urls import path
from . import views

urlpatterns = [
    path('add_comment_answer', views.add_comment_answer, name='add_comment_answer'),
]
