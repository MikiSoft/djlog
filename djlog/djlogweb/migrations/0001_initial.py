# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('post_author', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Djlog post',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Djlog posts',
            },
            bases=(models.Model,),
        ),
    ]
