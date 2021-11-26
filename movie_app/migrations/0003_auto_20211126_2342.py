# Generated by Django 3.2.9 on 2021-11-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20211126_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionsGener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='collections',
            name='genres',
            field=models.ManyToManyField(to='movie_app.Generes'),
        ),
        migrations.RemoveField(
            model_name='collections',
            name='movies',
        ),
        migrations.AddField(
            model_name='collections',
            name='movies',
            field=models.ManyToManyField(to='movie_app.Movie'),
        ),
    ]