from django.urls import path
from . import views

urlpatterns = [
    path('commentcreate/<int:blog_id>', views.commentcreate, name="commentcreate"),
]