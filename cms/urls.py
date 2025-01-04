from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.game_list, name='game-list'),
    path('games/<int:pk>/', views.game_detail, name='game-detail'),
    path('charts/', views.chart_list, name='chart-list'),
    path('charts/game/<int:pk>/', views.chart_list_in_game, name='game-chart'),
]