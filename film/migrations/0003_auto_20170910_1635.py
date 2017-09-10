# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20170910_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='by_link',
            field=models.CharField(null=True, verbose_name='下载链接1', max_length=800),
        ),
        migrations.AlterField(
            model_name='film',
            name='by_name',
            field=models.CharField(null=True, verbose_name='链接详情', max_length=800),
        ),
    ]
