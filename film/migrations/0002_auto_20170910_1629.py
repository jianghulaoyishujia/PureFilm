# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='name',
            field=models.CharField(verbose_name='电影名称', max_length=200, unique=True, null=True),
        ),
    ]
