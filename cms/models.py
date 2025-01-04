from django.db import models


# 楽曲に関するDB
class ArtistAlias(models.Model):
    """楽曲制作者名義 (合作にも対応) """
    alias_id = models.AutoField(primary_key=True)
    alias_name = models.CharField(max_length=255)
    def __str__(self):
        return self.alias_name

class Artist(models.Model):
    """楽曲制作者"""
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255)
    def __str__(self):
        return self.artist_name

class AliasToArtist(models.Model):
    """楽曲制作者名義と楽曲制作者の対応関係"""
    alias = models.ForeignKey(ArtistAlias, on_delete=models.CASCADE)
    creator = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.creator.artist_name} -> {self.alias.alias_name}"

class Music(models.Model):
    """楽曲情報"""
    music_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist_alias = models.ForeignKey(ArtistAlias, on_delete=models.CASCADE)
    bpm_max = models.FloatField()
    bpm_min = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title


# 音楽ゲームに関するDB
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=255)
    def __str__(self):
        return self.game_name

class Difficulty(models.Model):
    difficulty_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='difficulties')
    difficulty_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.difficulty_name} -> {self.game}"

class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='levels')
    level_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.level_name} -> {self.game}"

class ChartConstantToLevel(models.Model):
    constant_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='chart_constants')
    constant_value = models.FloatField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='chart_constants')
    def __str__(self):
        return f"{self.constant_value} -> {self.level} ({self.game})"


# 譜面に関するDB
class ChartCreatorAlias(models.Model):
    """譜面制作者名義 (合作にも対応)"""
    alias_id = models.AutoField(primary_key=True)
    alias_name = models.CharField(max_length=255)
    def __str__(self):
        return self.alias_name

class ChartCreator(models.Model):
    """譜面制作者"""
    creator_id = models.AutoField(primary_key=True)
    creator_name = models.CharField(max_length=255)
    def __str__(self):
        return self.creator_name

class ChartAliasToCreator(models.Model):
    """譜面制作者名義と譜面制作者の対応関係"""
    alias = models.ForeignKey(ChartCreatorAlias, on_delete=models.CASCADE)
    creator = models.ForeignKey(ChartCreator, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.creator.creator_name} -> {self.alias.alias_name}"

class Chart(models.Model):
    """譜面情報"""
    chart_id = models.AutoField(primary_key=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    creator_alias = models.ForeignKey(ChartCreatorAlias, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    chart_constant = models.ForeignKey(ChartConstantToLevel, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    added_date = models.DateField()
    def __str__(self):
        return f"{self.music}, {self.difficulty}"