# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djlogweb', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(to='djlogweb.Tag'),
            preserve_default=True,
        ),
    ]
