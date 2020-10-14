from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('alice/', views.alice),
    path('rabbit/', views.rabbit),
    path('cat/', views.cat),
    path('caterpillar/', views.caterpillar),
    path('duchess/', views.duchess),
    path('hat/', views.hat),
    path('queen/', views.queen),
    path('humdum/', views.humdum),
    path('poll/<int:poll_id>', views.poll, name="poll"),
    path('start/', views.start),
    path('final/', views.final),
    path('home/', views.home),
]