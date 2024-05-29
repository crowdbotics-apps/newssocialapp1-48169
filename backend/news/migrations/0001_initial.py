# Generated by Django 3.2.23 on 2024-05-29 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('is_trending', models.BooleanField(default='False')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved', models.BooleanField(default='False')),
                ('read_later', models.BooleanField(default='False')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userarticle_article', to='news.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userarticle_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]