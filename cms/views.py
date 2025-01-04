from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game, Chart
from .serializers import GameSerializer, ChartSerializer


@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        # データを取得してJSONレスポンス
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # 新しいゲームデータを作成
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found'}, status=404)

    if request.method == 'GET':
        serializer = GameSerializer(game)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        game.delete()
        return Response(status=204)

@api_view(['GET'])
def chart_list(request):
    if request.method == 'GET':
        charts = Chart.objects.all()
        serializer = ChartSerializer(charts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def chart_list_in_game(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found'}, status=404)

    if request.method == 'GET':
        charts = Chart.objects.filter(game=game)
        serializer = ChartSerializer(charts, many=True)
        return Response(serializer.data)
