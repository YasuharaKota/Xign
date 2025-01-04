from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.game_list, name='game-list'),
    path('games/<int:pk>/', views.game_detail, name='game-detail'),
    path('charts/', views.chart_list, name='chart-list'),
    path('charts/game/<int:game_pk>/', views.chart_list_in_game, name='game-chart'),
    path('charts/<int:chart_pk>/', views.chart_detail, name='chart-detail'),
    path('get_user_memo/<int:chart_pk>/', views.get_user_memo, name='get_user_memo'),
    path('upsert_user_memo/<int:chart_pk>/', views.upsert_user_memo, name='upsert_user_memo')
]