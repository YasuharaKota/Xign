from rest_framework import serializers
from .models import Game, Chart


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game_id', 'game_name']

class ChartSerializer(serializers.ModelSerializer):
    music = serializers.SerializerMethodField()
    creator_alias = serializers.SerializerMethodField()
    difficulty = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    chart_constant = serializers.SerializerMethodField()

    class Meta:
        model = Chart
        fields = ['chart_id', 'music', 'game', 'creator_alias', 'difficulty', 'level', 'chart_constant', 'comment']

    def get_music(self, obj):
        return {
            "title": obj.music.title,
            "artist_alias": obj.music.artist_alias.alias_name,
            "bpm_max": obj.music.bpm_max,
            "bpm_min": obj.music.bpm_min,
            "comment": obj.music.comment,
        }

    def get_creator_alias(self, obj):
        return {
            "alias_name": obj.creator_alias.alias_name,
        }

    def get_difficulty(self, obj):
        return {
            "difficulty_name": obj.difficulty.difficulty_name,
        }

    def get_level(self, obj):
        return {
            "level_name": obj.level.level_name,
        }

    def get_chart_constant(self, obj):
        return {
            "constant_value": obj.chart_constant.constant_value,
        }