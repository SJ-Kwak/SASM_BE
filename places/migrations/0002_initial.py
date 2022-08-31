# Generated by Django 4.0 on 2022-08-31 12:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_likeuser_set',
            field=models.ManyToManyField(blank=True, related_name='PlaceLikeUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
