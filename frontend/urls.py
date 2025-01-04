from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('games', index),  # /games でも React アプリが動作
    path('<int:pk>/charts/', index),
    path('<int:game_pk>/charts/<int:chart_pk>/', index),
]