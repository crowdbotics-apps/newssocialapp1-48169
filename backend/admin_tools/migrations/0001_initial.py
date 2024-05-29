# Generated by Django 3.2.23 on 2024-05-29 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentModeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('moderation_time', models.DateTimeField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentmoderation_article', to='news.article')),
                ('moderated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentmoderation_moderated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
