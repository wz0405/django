
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from user.views import home
urlpatterns = [
    path('detail/<int:pk>/',views.board_detail),
    path('list/',views.board_list),
    path('write/',views.board_write)
]
