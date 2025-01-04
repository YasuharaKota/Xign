# Generated by Django 5.1.4 on 2025-01-03 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistAlias',
            fields=[
                ('alias_id', models.AutoField(primary_key=True, serialize=False)),
                ('alias_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChartCreator',
            fields=[
                ('creator_id', models.AutoField(primary_key=True, serialize=False)),
                ('creator_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChartCreatorAlias',
            fields=[
                ('alias_id', models.AutoField(primary_key=True, serialize=False)),
                ('alias_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AliasToCreator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.artist')),
                ('alias_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.artistalias')),
            ],
        ),
        migrations.CreateModel(
            name='ChartAliasToCreator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.chartcreator')),
                ('alias_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.chartcreatoralias')),
            ],
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('difficulty_id', models.AutoField(primary_key=True, serialize=False)),
                ('difficulty_name', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='difficulties', to='cms.game')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.AutoField(primary_key=True, serialize=False)),
                ('level_name', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='cms.game')),
            ],
        ),
        migrations.CreateModel(
            name='ChartConstantToLevel',
            fields=[
                ('constant_id', models.AutoField(primary_key=True, serialize=False)),
                ('constant_value', models.FloatField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chart_constants', to='cms.game')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chart_constants', to='cms.level')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('music_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('bpm_max', models.FloatField()),
                ('bpm_min', models.FloatField()),
                ('comment', models.TextField()),
                ('artist_alias_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.artistalias')),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('chart_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('added_date', models.DateTimeField()),
                ('chart_constant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.chartconstanttolevel')),
                ('creator_alias_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.chartcreatoralias')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.difficulty')),
                ('game_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.game')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.level')),
                ('music_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.music')),
            ],
        ),
    ]
