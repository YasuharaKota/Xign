from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game, Chart, Memo
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
def chart_list_in_game(request, game_pk):
    try:
        game = Game.objects.get(pk=game_pk)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found'}, status=404)

    if request.method == 'GET':
        charts = Chart.objects.filter(game=game)
        serializer = ChartSerializer(charts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_user_memo(request, chart_pk):
    try:
        memo = Memo.objects.get(chart__chart_id=chart_pk)
        return Response({
            'one_liner_comment': memo.one_liner_comment,
            'detailed_comment': memo.detailed_comment,
        })
    except Memo.DoesNotExist:
        return Response({
            'one_liner_comment': '',
            'detailed_comment': '',
        })

@api_view(['GET'])
def chart_detail(request, chart_pk):
    try:
        chart = Chart.objects.get(chart_id=chart_pk)
    except Chart.DoesNotExist:
        return Response({'error': 'Chart not found'}, status=404)

    serializer = ChartSerializer(chart)
    return Response(serializer.data)

@api_view(['POST'])
def upsert_user_memo(request, chart_pk):
    try:
        # Chart インスタンスを取得
        chart = Chart.objects.get(chart_id=chart_pk)
    except Chart.DoesNotExist:
        return Response({'error': 'Chart not found'}, status=404)

    data = request.data  # 入力されたデータ
    memo, created = Memo.objects.get_or_create(chart=chart)

    # フィールドを更新
    memo.one_liner_comment = data.get('one_liner_comment', memo.one_liner_comment)
    memo.detailed_comment = data.get('detailed_comment', memo.detailed_comment)
    memo.save()

    return Response({
        'message': 'Memo updated' if not created else 'Memo created',
        'memo': {
            'one_liner_comment': memo.one_liner_comment,
            'detailed_comment': memo.detailed_comment,
        }
    })
