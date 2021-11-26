# Generated by Django 3.2.9 on 2021-11-26 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generesmoviemap',
            name='gen_id',
        ),
        migrations.RemoveField(
            model_name='generesmoviemap',
            name='movie_id',
        ),
        migrations.AddField(
            model_name='collections',
            name='movies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie_app.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie_app.generes'),
        ),
        migrations.DeleteModel(
            name='CollectionMovieMap',
        ),
        migrations.DeleteModel(
            name='GeneresMovieMap',
        ),
    ]
