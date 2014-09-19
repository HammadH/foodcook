# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import cooks.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(default=b'/home/dubizzle/projects/foodcook/foodcook/foodcook/media/default/profile1.png', upload_to=cooks.models.get_profile_image_path, max_length=1000, verbose_name=b'Profile picture', blank=True)),
                ('mobile', models.CharField(max_length=10, blank=True)),
                ('intro', models.TextField(blank=True)),
                ('place_slug', models.CharField(max_length=150, null=True)),
                ('breakfast', models.BooleanField()),
                ('lunch', models.BooleanField()),
                ('dinner', models.BooleanField()),
                ('min_price', models.IntegerField(null=True)),
                ('max_price', models.IntegerField(null=True)),
                ('place_info', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CookType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cuisines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=cooks.models.get_meal_image_path)),
                ('cook', models.ForeignKey(related_name=b'meals', to='cooks.Cook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MobileClickLead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cook', models.ForeignKey(to='cooks.Cook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cook',
            name='cook_type',
            field=models.ForeignKey(default=b'Unspecified', to='cooks.CookType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cook',
            name='cuisines',
            field=models.ManyToManyField(to='cooks.Cuisines'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cook',
            name='place',
            field=models.ForeignKey(blank=True, to='cooks.Place', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cook',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
